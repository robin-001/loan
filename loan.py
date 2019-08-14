import collections


def get_days_of_power(R1,D1,R2,D2,R3,D3,K):
    day_rates = {D1:R1,D2:R2,D3:R3}
    od = collections.OrderedDict(sorted(day_rates.items()))
    first_loan = od.popitem(last=False)
    start = first_loan[0]
    daily_rate=first_loan[1];
    days=0
    while True:
        K=K-daily_rate
        if  K<=0:
            break
        if start in od:
            daily_rate = daily_rate+od[start]
        start=start+1
        days=days+1
    return days