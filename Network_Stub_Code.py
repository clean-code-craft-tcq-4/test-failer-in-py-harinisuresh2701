Threshold_Temp = 100
def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # This is the real production code for network_alert
    # Return 200 for ok
    # Return 500 for not-ok
    if celcius < Threshold_Temp:
        return 200
    else :
        return 500
