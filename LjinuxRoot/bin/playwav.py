global NoAudio
if not NoAudio:
    try:
        with open(ljinux.based.user_vars["argj"].split()[1], "rb") as data:
            wav = WaveFile(data)
            a = PWMAudioOut(board.GP15)
            print("Playing")
            try:
                a.play(wav)
                while a.playing:
                    time.sleep(.2)
                    if ljinux.io.buttone.value:
                        if a.playing:
                            a.pause()
                            print("Paused")
                            time.sleep(.5)
                            while a.paused:
                                if ljinux.io.buttonl.value and ljinux.io.buttonr.value and not ljinux.io.buttone.value:
                                    a.stop()
                                elif ljinux.io.buttone.value:
                                    a.resume()
                                    print("Resumed")
                                    time.sleep(.5)
                                else:
                                    time.sleep(.1)
            except KeyboardInterrupt:
                a.stop()
            a.deinit()
            wav.deinit()
            print("Stopped")
    except OSError:
        ljinux.based.error(4)
else:
    print("No audio libraries loaded")
