from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.operator.crossover import PMXCrossover
from jmetal.operator.mutation import PermutationSwapMutation
from jmetal.problem.singleobjective.tsp import TSP
from jmetal.util.observer import PrintObjectivesObserver
from jmetal.util.termination_criterion import StoppingByEvaluations

if __name__ == "__main__":
    problem = TSP(instance="resources/TSP_instances/kroA100.tsp")

    print("Cities: ", problem.number_of_variables())

    algorithm = GeneticAlgorithm(
        problem=problem,
        population_size=100,
        offspring_population_size=100,
        mutation=PermutationSwapMutation(1.0 / problem.number_of_variables()),
        crossover=PMXCrossover(0.8),
        termination_criterion=StoppingByEvaluations(max_evaluations=250000),
    )

    algorithm.observable.register(observer=PrintObjectivesObserver(5000))

    algorithm.run()
    result = algorithm.get_result()

    print("Algorithm: {}".format(algorithm.get_name()))
    print("Problem: {}".format(problem.name()))
    print("Solution: {}".format(result.variables))
    print("Fitness: {}".format(result.objectives[0]))
    print("Computing time: {}".format(algorithm.total_computing_time))
