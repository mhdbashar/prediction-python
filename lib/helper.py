import re

orig_r=4
orig_c=7

#two hour in three day before
wind_r=2
wind_c=3

microservices_ts= {}
microservices_cfg= {}

def update_microservices_ts(key, value):
    # if key in microservices_ts:
    #     # diff=list(set(microservices_ts[key])-set(value))
    #     microservices_ts[key].extend(diff)  # If the key exists, append to the existing array
    # else:
    microservices_ts[key] = value # If the key doesn't exist, create a new array with the value

def update_microservices_cfg(key,history=orig_r,stepDuration=15,predictVerticalWindow=wind_r,predictHorizontalWindow=wind_c):
      microservices_cfg[key] = {
        "orig_r":int(re.search(r'\d+', history).group()), #orig_r
        "orig_c":int(60*24/int(re.search(r'\d+', stepDuration).group())), #to continue
        "wind_r":int(predictVerticalWindow), #wind_r
        "wind_c":int(predictHorizontalWindow) #wind_c
        } 
