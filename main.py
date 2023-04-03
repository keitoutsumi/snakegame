import ai_player
import game

pop_size=200
num_generations=20000
num_trials=1
window_size=7
hidden_size=15
board_size=10
gen_player = ai_player.GeneticPlayer(pop_size,num_generations,num_trials,window_size,hidden_size,board_size,mutation_chance=0.2,mutation_size=0.6)
gen_player.evolve_pop()

