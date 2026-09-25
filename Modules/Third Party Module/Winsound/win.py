import winsound

# Menu
print("========== WINSOUND MODULE ==========")
print("1. Simple Beep")
print("2. Different Beeps")
print("3. Play WAV File")
print("4. Play WAV File Asynchronously")
print("5. Message Beep")
print("6. Exit")

choice = int(input("Enter your choice: "))


# 1. Simple Beep
if choice == 1:

    # Beep(frequency, duration)
    # frequency -> sound ki frequency Hz mein
    # duration  -> sound kitni der chalegi, milliseconds mein

    winsound.Beep(1000, 500)

    print("Simple beep played.")


# 2. Different Beeps
elif choice == 2:

    # Alag-alag frequency ke beep
    # Frequency badhne par sound zyada high-pitched hoti hai

    winsound.Beep(500, 300)
    winsound.Beep(1000, 300)
    winsound.Beep(1500, 300)

    print("Different beeps played.")


# 3. Play WAV File
elif choice == 3:

    # PlaySound(sound, flags)
    #
    # sound -> kaunsi .wav file play karni hai
    # flags -> file ko kaise play karna hai
    #
    # SND_FILENAME ka matlab:
    # sound ko ek filename/path maana jayega

    winsound.PlaySound(
        "huamain.wav",
        winsound.SND_FILENAME
    )

    print("Sound file played.")


# 4. Play WAV File Asynchronously
elif choice == 4:

    # SND_ASYNC ka matlab:
    # sound play hoga lekin program sound khatam hone ka wait nahi karega

    winsound.PlaySound(
        "huamain.wav",
        winsound.SND_FILENAME | winsound.SND_ASYNC
    )

    print("Sound started asynchronously.")


# 5. Message Beep
elif choice == 5:

    # MessageBeep() Windows ka default message sound play karta hai

    winsound.MessageBeep()

    print("Message beep played.")


# 6. Exit
elif choice == 6:

    print("Program closed.")


# Invalid choice
else:

    print("Invalid choice!")