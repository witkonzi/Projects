class BusStop:

    def __init__(self,name:str,change_pos:bool,stop_time:tuple) -> None:
        self._name = name
        self._change_pos = change_pos
        self._stop_time = stop_time

    def get_name(self) -> str:
        return self._name

    def get_stop_time(self) -> tuple:
        return self._stop_time

    def get_change_pos(self):
        return self._change_pos

class RoutePosition:

    def __init__(self, bus_stop: BusStop, time_between_bus_stops: int) -> None:
        self._bus_stop = bus_stop
        self._time_between_bus_stops = time_between_bus_stops

    def get_change_pos_bus_stop(self):
        return self._bus_stop.get_change_pos()

    def get_bus_stop_name(self) -> str:
        return self._bus_stop.get_name()

    def get_bus_stop_stop_time(self) -> tuple:
        return self._bus_stop.get_stop_time()

    def get_time_between_bus_stops(self):
        return self._time_between_bus_stops

    def get_time_of_set_off(self) -> tuple:
        if self._bus_stop.get_stop_time()[1] + self._time_between_bus_stops >= 60:
            hour = self._bus_stop.get_stop_time()[0] + 1
            minutes = (self._bus_stop.get_stop_time()[1] + self._time_between_bus_stops) //60
            return hour,minutes

class Route:

    def __init__(self,name:str,list_of_route_positions:list) -> None:
        self._name = name
        self._list_of_route_positions = list_of_route_positions

    def generate_time_table(self, time: tuple):
        print(f'Name of the route : {self._name}')
        list_for_bus_stops_to_print : list = []
        for bus_stops in self._list_of_route_positions:
            if (time[0] == bus_stops.get_bus_stop_stop_time()[0]) and (time[1] > bus_stops.get_bus_stop_stop_time()[1]):
                list_for_bus_stops_to_print.append(bus_stops)
            elif time[0] < bus_stops.get_bus_stop_stop_time()[0]:
                list_for_bus_stops_to_print.append(bus_stops)
        print(f'Start time of route : {list_for_bus_stops_to_print[0].get_bus_stop_stop_time()[0]}.{list_for_bus_stops_to_print[0].get_bus_stop_stop_time()[1]}')
        print(f'End time of route : {list_for_bus_stops_to_print[-1].get_bus_stop_stop_time()[0]}.{list_for_bus_stops_to_print[-1].get_bus_stop_stop_time()[1]}')
        for elements in list_for_bus_stops_to_print:
            print(f'Station : {elements}')
            print(f'Arrival time : {elements.get_bus_stop_stop_time()[0]}.{elements.get_bus_stop_stop_time()[1]}')
            print(f'Set off time : {elements.get_time_of_set_off()[0]}.{elements.get_time_of_set_off()[1]}')
            print(f'Possibility to change : {"Yes" if elements.get_change_pos_bus_stop() else "No"}')