def get_info_from_reg_form(originalfile, html_file):
	# def get_info_from_reg_form(originalfile, html_file):
	with open(originalfile, 'r') as formfile:
		forminfo = formfile.read().strip()
		#find host name
		end_IBM_host = forminfo.find('IBM Host email:') - 1
		host_name = forminfo[263:end_IBM_host].strip()
		#find start time
		beginning_start_time = forminfo.find('Meeting Start Time:') + 19
		ending_start_time = forminfo.find('End Time:') - 1
		start_time = forminfo[beginning_start_time:ending_start_time].strip()
		#find end time
		beginning_end_time = forminfo.find('End Time:') + 9
		ending_end_time = forminfo.find('Will you require any set-up time prior to the start of the meeting?') - 1
		end_time = forminfo[beginning_end_time:ending_end_time].strip()
		#find purpose
		beginning_purpose = forminfo.find('PURPOSE OF THE EVENT') + 20
		end_purpose = forminfo.find('CLIENT INFORMATION') - 1
		purpose = forminfo[beginning_purpose:end_purpose].strip()
		#make purpose lowecase for intro
		intro_purpose = purpose.lower()
		#find client name
		beginning_client_name = forminfo.find('Client Name :') + 13
		end_client_name = forminfo.find('Revenue Influenced by Event') - 1
		client_name = forminfo[beginning_client_name:end_client_name].strip()
		#find av
		beginning_av = forminfo.find('VISUAL REQUIREMENTS') + 20
		end_av = forminfo.find('OTHER REQUIREMENTS') - 1
		av = forminfo[beginning_av:end_av]
		#find catering
		begining_catering = forminfo.find('card number):') + 14
		end_catering = forminfo.find('Dietary Restrictions') - 1
		catering = forminfo[begining_catering:end_catering].strip()
		if catering == "No Catering Requirements":
			catering = 'None'
		else:
			catering = "Yes, see folder for details"
		html = """
		<head>
			<style>
				.body{
					font-family: "Default Sans Serif";
					font-size: 10px
				}
			</style>
		</head>
		<body>
			<p>
				Hello Everyone, <br>
				<br>
				Below is the information for tomorrow's {6}.  If you have any questions or concerns, please let me know. <br>
				<br>
				Thanks,
				<br>
				Maggie 
				<br>
				<br>
			</p>
			<p>
				<strong>Attendees:</strong>
				<br>
				<br>
				<br>
			</p>	
			<p>
				<strong>Schedule: </strong>{1} - {2}
			</p>
			<p>
				<strong>Purpose: </strong>{3}
			</p>
			<p>
				<strong>Agenda: </strong>None Provided
			</p>
			<br>
			<br>
			<p>
				<strong>IEG REQUIREMENTS</strong>
			</p>
			<p>
				<strong>Meeting Room:</strong>
			</p>
			<p>
				<strong>Audio/Visual:</strong>{4}
			</p>
			<p>
				<strong>Other:</strong>
			</p>
			<p>
				<strong>Marquee: </strong>Welcome {0}
			</p>
			<p>
				<strong>Sign-in: </strong>Upon arrival at the front door
			</p>
			<p>
				<strong>Catering: </strong>{5}
			<p>
				<strong>Event Manager: </strong>
			</p>
		</body>
		""".format(client_name, start_time, end_time, purpose, av, catering, intro_purpose)
		with open(html_file, 'w') as htmlfile:
			htmlfile.write(html)
			htmlfile.close()
input_file = raw_input("What is the name of your text file?")
output_file = raw_input("What do you want the name of the html file to be?")
get_info_from_reg_form(input_file, output_file)	
