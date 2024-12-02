import random

"""
Punktacja:
Para - wynik na kostce * 2 (para czwórek = 8 pkt)
Trójka - wynik na kostce * 4 (trójka dwójek = 8 pkt)
Kareta - wynik kostce * 6 (czwórka jedynek = 6 pkt)
Same cyfry parzyste - suma oczek + 2
Same cyfry nieparzyste - suma oczek + 3
(w przypadku gdy jednocześnie występuje 
np. para i wszystkie cyfry są parzyste, bierzemy pod uwagę lepszy wynik punktowy. 
Przykład: dla układu [6,6,6,2] mamy trójkę szóstek wartą 26 pkt i 
same cyfry parzyste warte 22 pkt, czyli cały układ ma wartość 26 pkt)
"""

"""Functions rules_for_dices returns score for each drawn_values"""
def rules_for_dices(drawn_values : list) -> int:
    score = 0
    dict_numbers = {element: numbers.count(element) for element in set(numbers)}

    def get_key(val):
        for key, value in dict_numbers.items():
            if val == value:
                return key
        else :
            return f'not existing key'

    def if_all_even(list_val : list) -> bool:
        if all(number % 2 == 0 for number in numbers):
            return True
        else :
            return False
         
    def if_all_odd(list_val : list) -> bool:
        if all(number % 2 == 1 for number in numbers):
             return True
        else :
             return False

    if 3 in dict_numbers.values():
        score_3 = sum(numbers) + get_key(3)
        if if_all_even(numbers):
            score_even = sum(numbers) + 2
            if score_even > score_3:
                return score_even
            else :
                return score_3
        elif if_all_odd(numbers):
            score_odd = sum(numbers) + 3
            if score_odd > score_3:
                return score_odd
            else :
                return score_3
        else : 
            return score_3
        
    if 4 in dict_numbers.values():
        score_4= sum(numbers) + 2*get_key(4)
        if if_all_even(numbers):
            score_even = sum(numbers) + 2
            if score_even > score_3:
               return score_even
            else :
                return score_4
        elif if_all_odd(numbers):
            score_odd = sum(numbers) + 3
            if score_odd > score_4:
                return score_odd
            else :
               return score_4
        else : 
            return score_4
    else : 
        score = sum(numbers)
        return score
    
class Player:
    
    def __init__(self,name: str,combination_of_dices : list , score : int = 0) -> None:
        self._name = name
        self._combination_of_dices = combination_of_dices
        self._score = score
        
    def get_name(self) -> str:
        return self._name
        
    def get_combination_of_dices(self,combination_of_dices) ->list:
        return self._combination_of_dices    
    
    def set_combination_of_dices(self,combination_of_dices) -> None:
        self._combination_of_dices = combination_of_dices
    
    def get_score(self) -> int:
        return self._score
        
    def set_score(self,score) -> None:
        self_score = score
        
class Casino:
    
    def __init__(self, list_of_players: list) -> None:
        self._list_of_players = list_of_players
        
    def get_list_of_players_names(self) -> list:
        list_of_players_names : list = []
        for player_object in self._list_of_players:
            list_of_players_names.append(player_object.get_name())
        for player_name in list_of_players_names:
            print(player_name)
            
    def add_player(self,player : Player):
        if player in self._list_of_players:
            raise ValueError ("Player already in list")
        else :
            self._list_of_players.append(player)
        
    def remove_player(self,player : object) -> None:
        if player not in self._list_of_players:
            raise ValueError ("Player not in list")
        else : 
            self._list_of_players.remove(player)
                
    def throw_dices(self) -> None:
        drawn_values : list = [random.randint(1,7) for number_of_dices in range(4)]
        dict_of_players : dict = {player: drawn_values for player in self._list_of_players}
        for player in self._list_of_players:
            player.set_combination_of_dices(dict_of_players[player])
            player.set_score(rules_for_dices(player.get_combination_of_dices()))
    
    def winner(self) -> str:
        list_of_scores : list = []
        for player in self._list_of_players:
            list_of_scores.append(player.get_score())
        winning_score = max(list_of_scores)
        for player in self._list_of_players:
            if player.get_score() == winning_score:
                return player.get_name()
        


