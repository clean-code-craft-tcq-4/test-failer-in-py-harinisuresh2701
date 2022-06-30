import alerter
alert_failure_count = 0
Threshold_temp = 100
alerter.alert_in_celcius(400.5,alerter.network_alert_stub)
alerter.alert_in_celcius(303.6,alerter.network_alert_stub)
assert alert_failure_count == 2
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
