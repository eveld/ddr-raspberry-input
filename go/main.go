package main

import (
	"net/http"
	"runtime"
	"time"

	"github.com/micmonay/keybd_event"
)

func main() {
	kb, err := keybd_event.NewKeyBonding()
	if err != nil {
		panic(err)
	}

	// For linux, it is very important wait 2 seconds
	if runtime.GOOS == "linux" {
		time.Sleep(2 * time.Second)
	}

	http.HandleFunc("/", func(rw http.ResponseWriter, r *http.Request) {
		//set keys
		kb.SetKeys(keybd_event.VK_Q)
		//set shif is pressed
		kb.(true)

		//launch
		err = kb.Launching()
		if err != nil {
			panic(err)
		}
	})

	http.ListenAndServe(":8000", nil)
	//Ouput : AB
}
