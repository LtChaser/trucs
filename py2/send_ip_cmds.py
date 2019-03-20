import json

init_logging(d['environment']['run_uuid'], d['module'])

stbip='192.168.192.2'

request = Request('http://127.0.0.1/api/v2/devices/' + d["environment"]["device_uuid"]) # call device API
response_body = urlopen(request).read()
try:
    output = json.loads(response_body)
except ValueError as e:
     logging.exception('ValueError: %s', e)

#logging.debug("response_body: %s ", output)

success = True

found = False

try:
    device_properties = json.loads(output['properties'])
except ValueError as e:
    logging.exception('ValueError: %s', e)

logging.debug("device_properties: %s ", output['properties'])

for custom_property in device_properties['properties_attributes'] :
	if custom_property['key'] =='stbip' : #check if the desired custom property key is there
		stbip = custom_property['value'] #store the value of the property
                                
		found = True
		break

# connect to stb
logging.debug("Connecting to: %s ", stbip)
s = init_connect(stbip)

wait = 200
if d["wait"] != None :
  wait = int(d["wait"])

if s is not None :
  for key in d["keys"][:-1] :
     success = success and send_one_key(s,key)
     time.sleep(float(wait) / 1000)
  success = success and send_one_key(s,d["keys"][-1])
else :
  success = False

# close connect
end_connect(s)

ret_dict = {}

if success :
  ret_dict["returncode"] = 0 # set to 1 to output on the FAILURE output
else :
  ret_dict["returncode"] = 1

return ret_dict
