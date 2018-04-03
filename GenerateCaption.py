import cloudsight
import GenerateVoice as GV
import time
def Caption(image_name, passs):
	auth=cloudsight.SimpleAuth(passs)
	api = cloudsight.API(auth)	
	Filter_chocolate = ['chocolate']
	filter_phone=['smartphone', 'phone', 'mobile', 'Smartphone', 'Phone' ,'Mobile']
	with open(image_name, 'rb') as f:
		response = api.image_request(f, image_name, {
			'image_request[locale]': 'en-US',
		})
	status = api.wait(response['token'], timeout=30)
	status = api.image_response(response['token'])
	if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
		try:
			caption = status['name']
			for content in Filter_chocolate:
				if content in caption:
					print('Warning: Eating Cholocate is injurious to Health') 
					GV.speak('Warning: Eating Cholocate is injurious to Health.... Image Content')
					break
			for content in filter_phone:
				if content in caption:
					print("Alert: %s Detected.. Filtered Content.." %content)
					GV.speak("Alert: %s Detected.. Filtered Content.." %content)
					return
			print(caption)
			GV.speak(caption)
			return(caption)
		except:
			print('Cannot Process this image')
	else:
		print('Cannot Process Image')

if __name__ == '__main__':
	#Caption('try.jpg', '2LczFk27N0WOxYnhF123Zg')
	Caption('try.jpg', '_XQLIiTlbfyHEDJYOwEktQ')