print("""
Welcome to Nokia02,simplicity is life
********************Menu Functions********************
1.Phone book
2.Messages
3.Chat
4.Call register
5.Tones
6.Setting
7.Call divert
8.Music
9.Games
10.Calculator
11.Reminders
12.Clock
13.Profiles
14.Services
15.SIM services
""")

mainmenu_entry=int(input("Enter any number from 1 to 15: "))
match mainmenu_entry:
	case 1:
		print("Phone book")
		phonebook_entry=int(input("Enter any number from 1 to 11: "))
		match phonebook_entry:
			case 1:
				print("Services")
			case 2:
				print("Service Nos")
			case 3:
				print("Add name")
			case 4:
				print("Erase")
			case 5:
				print("Edit")
			case 6:
				print("Copy")
			case 7:
				print("Assign tone")
			case 8:
				print("Send b'card")
			case 9:
				print("Options")
				print("""
				1.Memory in use
				2.Type of view
				3.Memory status
				""")
				options_choice=int(input("Pick a number between 1 to 3: "))
				match options_choice:
						case 1:
							print("Memory in use")
						case 2:
							print("Type of view")
						case 3:
							print("Memory status")
			case 10:
				print("Speed dials")
			case 11:
				print("Voice tags")

	case 2:
		print("Messages")
		message_entry=int(input("Enter any number between 1 to 10: "))
		match message_entry:
			case 1:
				print("Write messages")
			case 2:
				print("Inbox")
			case 3:
				print("Outbox")
			case 4:
				print("Picture messages")
			case 5:
				print("Templates")
			case 6:
				print("Smileys")
			case 7:
				print("Message settings")
				print("""
				1.set 1
				2.Common
				""") 
				messagesettings_entry=int(input("Pick a number between 1 or 2: "))
				match messagesettings_entry:
					case 1:
						print("Set 1")
						print("""
						1.Message center number
						2.Message sent as
						3.Message validity
						""")
						
						set1_entry=int(input("Pick a number between 1 to 3: "))
						match set1_entry:
							case 1:
								print("Message centre number")
							case 2:
								print("Message sent as")
							case 3:
								print("Message Validity")
					case 2:
						print("Common")
						print("""
						1.Delivery reports
						2.Reply via same centre
						3.Character support
						""")

						
						common_entry=int(input("Pick a number between 1 to 3: "))
						match common_entry:
							case 1:
								print("Delivery reports")
							case 2:
								print("Reply via same centre")
							case 3:
								print("Character support")
			case 8:
				print("Info service")
			case 9:
				print("Voice mailbox number")
			case 10:
				print("Service command editor")
	case 3:
		print("Chat")
	case 4:
		print("Call register")
		print("""
		1.Missed calls
		2.Recieved calls
		3.Dialled numbers
		4.Erase recent call lists
		5.Show call duration
		""")
		callregister_entry=int(input("Enter any number between 1 to 8: "))
		match callregister_entry:
			case 1:
				print("Missed calls")
			case 2:
				print("Recieved calls")
			case 3:
				print("Dialled numbers")
			case 4:
				print("Erase recent call lists")
			case 5:
				print("Show call duration")
				print("""
				1.Last call duration
				2.All calls' duration
				3.Recieved calls' duration
				4.Dialled calls' duration
				5.Clear timers
				""")
				callduration_entry=int(input("Pick a number between 1 to 5: "))
				match callduration_entry:
					case 1:
						print("Last call duration")
					case 2:
						print("All calls' duration")
					case 3:
						print("Recieved calls' duration")
					case 4:
						print("Dialled calls' duration")
					case 5:
						print("Clear timers")


			case 6:
				print("Show call cost")
				print("""
				1.Last call cost
				2.All calls' duration
				3.Clear counters
				""")
				callcost_entry=int(input("Pick a number between 1 to 3: "))
				match callcost_entry:
					case 1:
						print("Last call cost")
					case 2:
						print("All calls' cost")
					case 3:
						print("Clear counters")
			case 7:
				print("Call cost settings")
				print("""
				1.Call cost limit
				2.Show costs in
				""")
				costsetting_entry=int(input("Pick a number between 1 or 2: "))
				match costsetting_entry:
					case 1:
						print("Call cost limit")
					case 2:
						print("Show costs in")
			case 8:
				print("Prepaid credit")


	case 5:
		print("Tones")
		print("""
		1.Ringing tone
		2.Ringing Volume
		3.Incoming call alert
		4.Message alert tone
		5.Keypad tones
		6.Warning tones
		7.Vibrating alert
		8.Screen saver
		""")
		tones_entry=int(input("Enter a number between 1 to 8: "))
		match tones_entry:
			case 1:
				print("Ringing tone")
			case 2:
				print("Ringing Volume")
			case 3:
				print("Incoming call alert")
			case 4:
				print("Message alert tone")
			case 5:
				print("Keypad tones")
			case 6:
				print("Warning tones")
			case 7:
				print("Vibrating alert")
			case 8:
				print("Screen saver")


		
	case 6:
		print("Settings")
		print("""
		1.Call settings
		2.Phone settings
		3.Security settings
		4.Restore factory setting
		""")
		setting_entry=int(input("Pick a number between 1 and 4: "))
		match setting_entry:
			case 1:
				print("Call settings")
				print("""
				1.Automatic redial
				2.Speed dialling
				3.Call waiting options
				4.Own number sending
				5.Phone line in use
				6.Automatic answer
				""")
				callsetting_entry=int(input("Pick a number between 1 to 6: "))
				match callsetting_entry:
					case 1:
						print("Automatic redial")
					case 2:
						print("Speed dialling")
					case 3:
						print("Call waiting options")
					case 4:
						print("Own number sending")
					case 5:
						print("Phone line in use")
					case 6:
						print("Automatic answer")


			case 2:
				print("Phone settings")
				print("""
				1.Language
				2.Cell info display
				3.Welcome note
				4.Network selection
				5.Confirm SIM service actions
				""")
				phonesetting_entry=int(input("Pick a number between 1 to 5: "))
				match phonesetting_entry:
					case 1:
						print("Language")
					case 2:
						print("Cell info display")
					case 3:
						print("Welcome Note")
					case 4:
						print("Network selection")
					case 5:
						print("Confirm SIM service actions")

			case 3:
				print("Security settings")
				print("""
				1.Print code request
				2.Call barring service
				3.Fixed dialling
				4.Closed user group
				5.Security level
				6.Change access codes
				""")

				securitysetting_entry=int(input("Pick a number between 1 to 6: "))
				match securitysetting_entry:
					case 1:
						print("PIN code request")
					case 2:
						print("Call barring service")
					case 3:
						print("Fixed dialling")
					case 4:
						print("Closed user group")
					case 5:
						print("Security level")
					case 6:
						print("Change access codes")

			case 4:
				print("Restore factory settings")

	case 7:
		print("Call divert")
	case 8:
		print("Music")
		print("""
		1.Music player
		2.Radio
		3.Recorder
		4.Track list
		""")
		music_entry=int(input("Pick a number between 1 to 4: "))
		match music_entry:
			case 1:
				print("Music player")
			case 2:
				print("Radio")
			case 3:
				print("Recorder")
			case 4:
				print("Track list")

	case 9:
		print("Games")
	case 10:
		print("Calculator")
	case 11:
		print("Reminders")
	case 12:
		print("Clock")
		print("""
		1.Alarm clock
		2.Clock settings
		3.Date setting
		4.Stop watch
		5.Countdown timer
		6.Auto update of date and time
		""")
		clock_entry=int(input("Pick a number between 1 to 6: "))
		match clock_entry:
			case 1:
				print("Alarm clock")
			case 2:
				print("Clock settings")
			case 3:
				print("Date setting")
			case 4:
				print("Stop watch")
			case 5:
				print("Countdown timer")
			case 6:
				print("Auto update of date and time")
	case 13:
		print("Profiles")
	case 14:
		print("Services")
	case 15:
		print("SIM services")

 