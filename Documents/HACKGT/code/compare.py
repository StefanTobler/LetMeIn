import http.client, urllib.request, urllib.parse, urllib.error

def get_confidence():
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '<key here>',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false'
    })

    #keeps track of image count
    file = open('index.txt', 'r')
    num = str(file.readline()).replace(' ', '').replace('\n', '')
    num = str(int(num) + 1)
    file.close()

    #increments image count so that the url can change each time
    #without this, the API assumes that the same face is present
    file = open('index.txt', 'w')
    file.write(str(int(num)))
    file.close()

    params1 = urllib.parse.urlencode({
    })
    url = 'image url'.format(num)

    try:
        conn = http.client.HTTPSConnection('[location].api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params,
         "{'url': '%s'}" % url, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    #gets the face ID from the byte array response
    my_json = data.decode('utf8').replace("'", '"')
    faceid = my_json.find('faceId')
    facerec = my_json.find('faceR')
    id = my_json[faceid+9:facerec-3]

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '<key here>',
    }

    params = urllib.parse.urlencode({
    })


    try:
        conn = http.client.HTTPSConnection('[location].api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/identify?%s" % params,
         '{"faceIds": ["%s"], "personGroupId": "roommates"}' % id,
         headers)
        response = conn.getresponse()
        data = response.read()
        #print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    #uses patterns in the response to get the confidence from the byte array response
    #using string splicing
    my_json = data.decode('utf8').replace("'", '"')

    #finds confidence from byte array response
    confidence = my_json.find('confidence')
    facerec = my_json.find('faceR')
    confidence = my_json[confidence +12:-4]

    #returns 1 or 0, based on whether the confidence of the result is greater than
    #what is desired by the user.
    #If the API doesn't think there's any similarity, or there's no face, no match is suggested
    #so the return value is -1
    try:
        desired_confidence = .7
        if float(confidence) > desired_confidence:
            return 1
        else:
            return 0
    except:
        return -1
