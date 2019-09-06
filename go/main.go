package main

import (
	"encoding/json"
	"net/http"
	"runtime"
	"time"

	"github.com/gorilla/mux"
	"github.com/micmonay/keybd_event"
)

var keys = map[string]int{
	"vault":     keybd_event.VK_Q,
	"consul":    keybd_event.VK_W,
	"terraform": keybd_event.VK_E,
	"nomad":     keybd_event.VK_A,
	"vagrant":   keybd_event.VK_S,
	"packer":    keybd_event.VK_D,
}

var kb keybd_event.KeyBonding

func pressHandler(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	tile := vars["tile"]

	//set keys
	key := keys[tile]
	kb.SetKeys(key)

	//launch
	err := kb.Launching()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	out := json.NewEncoder(w)
	out.Encode("pressed " + tile)
}

func main() {
	var err error
	kb, err = keybd_event.NewKeyBonding()
	if err != nil {
		panic(err)
	}

	// For linux, it is very important wait 2 seconds
	if runtime.GOOS == "linux" {
		time.Sleep(2 * time.Second)
	} else {
		// force OSX to register update
		kb.SetKeys(keybd_event.VK_0)

		//launch
		err = kb.Launching()
		if err != nil {
			panic(err)
		}
	}

	router := mux.NewRouter()
	router.HandleFunc("/touch/{tile}", pressHandler).Methods(http.MethodPost)
	http.ListenAndServe(":9090", router)
}
