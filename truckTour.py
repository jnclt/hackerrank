def truckTour(petrolpumps):
    start_pump = 0
    reached_pump = 0
    petrol = 0
    while reached_pump < len(petrolpumps) - 1:
        petrol += petrolpumps[reached_pump][0] - petrolpumps[reached_pump][1]
        reached_pump += 1
        if petrol < 0:
            start_pump = reached_pump
            petrol = 0
    return start_pump