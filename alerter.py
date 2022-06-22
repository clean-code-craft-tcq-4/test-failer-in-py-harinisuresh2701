import Network_Stub_Code
alert_failure_count = 0
Threshold_temp = 100
def network_alert_main_code(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200 :
    if celcius < Threshold_temp :
        return 200
    else:
        return 500

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = Network_Stub_Code.network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0
        
alerter.alert_in_celcius(400.5)
alerter.alert_in_celcius(303.6)
assert alert_failure_count == 2
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
