"""
Contact mechanics sub models (:mod:`slippy.contact.sub_models`)
===============================================================

.. currentmodule:: slippy.contact.sub_models

In slippy, things that are not solved in the main normal contact loop are dealt with using sub models. These could be
anything from flash temperature to tribofilm growth to friction etc.. These sub models cover behaviour that doesn't
need to be strongly coupled to the normal contact problem or acts on a slower time scale.

Currently implemented sub models are:

.. autosummary::
   :toctree: generated

   ResultContactStiffness       -- Find contact stiffness in any direction
   WearElasticPerfectlyPlastic  -- Wear the surfaces where there is excess interference after elastic deformation

"""

from .contact_stiffness import ResultContactStiffness
from .epp_wear import WearElasticPerfectlyPlastic
from .friction_coulomb_model import FrictionCoulombSimple
from .tangential_pure_sliding import TangentialPureSliding
from .tangential_partial_slip import TangentialPartialSlip

__all__ = ['ResultContactStiffness', 'WearElasticPerfectlyPlastic', 'FrictionCoulombSimple', 'TangentialPureSliding',
           'TangentialPartialSlip']
