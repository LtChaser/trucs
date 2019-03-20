def init_logging(run_uuid, module) :

   global logging_done

   if not logging_done :
      logfile  = os.getenv('WITBELOGSSTORAGE') + '\\witbe-scenario-engine\\' + run_uuid + '\\' + module + '.log'
      logging.basicConfig(filename=logfile,level=logging.DEBUG,format = '%(asctime)s %(levelname)-8s | %(message)s', datefmt='%Y%m%d %H:%M:%S')
      logging_done = True

   return

def send_one_key(s, key) :

    kc = key_dict.get(key)
    if kc is None :
      return False

    logging.debug("Sending keyCode: %s", kc.encode('hex'))
    
    mt = '\x04' # message type for keyEvent
    kd = '\x01' # key pressed
    ku = '\x00' # key released
    p = '\x00\x00\x00\x00' # padding
    code = True
    try :
      s.send( mt + kd + p + kc)
      s.send( mt + ku + p + kc)
    except: 
      code = False
    return code

def init_connect(host) :

   try :
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.connect((host, 5900))
       # receive and echo the version: "RFB 003.008\n"
       answer = s.recv(12)
       logging.debug("Version: %s", answer)
       s.send(answer)

       # receive number of schemes + the security schemes: '\x01\x01'
       answer = s.recv(8)
       logging.debug("Security scheme: %s", answer.encode('hex'))
       s.send('\x01')  # None security

       # receive security result: '\x00\x00\x00\x00'
       answer = s.recv(4)
       logging.debug("Security result: %s", answer.encode('hex'))
       # Send client initialisation shared flag
       s.send('\x01')  # shared

       # receive Server intitializaton: display settings (not used on Horizon)
       answer = s.recv(24)
       logging.debug(answer.encode('hex'))
       return s

   except :
       logging.exception("Error to init_connect")
       return None

def end_connect(s) :
    try: 
        close(s)
    except:
        pass
    return None