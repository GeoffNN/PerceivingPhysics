"""Using MCMC to find the physics of a video - after object recognition"""

import numpy as np
from numpy.lib.scimath import arccos
from scipy.spatial.distance import euclidean
from scipy.stats import bernoulli, uniform

from pendulum_sim.physics_engine import SimplePendulum
from video_processing.find_center import find_pivot


def random_walk(f='../../data/m_hist.csv', n_walks=20, walk_len=75):
    # Is it better to have a smart initial guess ?
    guesses = []
    probas = np.zeros(n_walks)
    measures = get_measures(f)
    guess = initial_guess(f)
    guess_pendulum = SimplePendulum(*guess)
    sim_measures = [guess_pendulum.simulate() for _ in range(len(measures))]
    prob = likelihood(measures, sim_measures)
    for j in range(n_walks):
        for k in range(walk_len):
            if k % 20 == 0:
                new_guess = guess + uniform.rvs(-.5, 0.5, len(guess))
            else:
                new_guess = guess + uniform.rvs(-.05, 0.05, len(guess))

            new_sim_measures = SimplePendulum(*new_guess).simulate()
            new_prob = likelihood(measures, new_sim_measures)
            alpha = new_prob / prob
            if alpha >= 1 or bernoulli.rvs(alpha) == 1:
                guess = new_guess
                prob = new_prob
        guesses.append(guess)
        probas[j] = prob
    return guesses[probas.argmax()]


def likelihood(measures, simulated_measures):
    return np.exp(-cost(measures, simulated_measures))


def cost(measures, simulated_measures):
    return euclidean(measures, simulated_measures)


def initial_guess(f='../../data/m_hist.csv'):
    # Take in only one period of data
    # f must contain predictions from object recognition model
    guessed_len, guessed_pivot, m_pos_hist = find_pivot(f)
    rel_pos_hist = m_pos_hist - guessed_pivot
    guessed_theta = arccos(rel_pos_hist[:, 0], rel_pos_hist[:, 1])
    guessed_theta_dot = guessed_theta[1] - guessed_theta[:-2]
    guessed_restitution = 1
    guessed_radius = 50
    # guessed_radius = 20 ball_tracking.radius TODO: implement this - but no one cares
    guessed_m = 50 # TODO : smarter guess than this
    return np.array(guessed_m, guessed_len, guessed_radius, guessed_pivot, guessed_theta[0], guessed_theta_dot[0],
                    guessed_restitution)


def get_measures(f):
    # TODO: implement to get a period of measures from file f
    pass
