from autode import *

Config.n_cores = 4
Config.path_to_orca = '/usr/local/orca_4_1_1/orca'
Config.path_to_xtb = '/usr/local/xtb/bin/xtb'

flouride = Reactant(name='F-', smiles='[F-]', solvent='water')
methyl_chloride = Reactant(name='CH3Cl', smiles='[H]C([H])(Cl)[H]', solvent='water')
chloride = Product(name='Cl-',  smiles='[Cl-]', solvent='water')
methyl_flouride = Product(name='CH3F', smiles='[H]C([H])(F)[H]', solvent='water')

reaction = Reaction(flouride, methyl_chloride, chloride, methyl_flouride)
reaction.calculate_reaction_profile()