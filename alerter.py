alert_failure_count = 0
Threshold_temp = 100
def network_alert_main_code(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200 :
    if celcius < 100 :
        return 200
    else:
        return 500
def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # This is the real production code for network_alert
    # Return 200 for ok
    # Return 500 for not-ok
    if celcius < 100:
        return 200
    else :
        return 500

def alert_in_celcius(farenheit,network_alerter_code):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alerter_code(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1
        
alert_in_celcius(400.5,network_alert_stub)
alert_in_celcius(303.6,network_alert_stub)
assert alert_failure_count == 2
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
