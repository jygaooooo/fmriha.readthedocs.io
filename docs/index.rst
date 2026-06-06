.. image:: static/fmriha_logo.png
   :alt: fMRI-HA logo
   :width: 200px
   :align: left

*fMRI-HA*: A Python-Based Workflow for fMRI Hyperalignment
=======

.. raw:: html

   <div style="clear: both;"></div>

About
-----

``fMRI-HA`` is a modular Python toolkit for functional magnetic resonance imaging (fMRI) 
hyperalignment and related analyses. It is designed to support common fMRI
workflows including preprocessing, searchlight generation, response-based
hyperalignment, connectivity-based hyperalignment, transformation into common
spaces, downstream statistical analysis, and pipeline script generation. These
workflows are provided in both script-based and GUI-based versions for
configuring and running major analyses.

The package is being organized as a reusable research toolkit so that users can
run end-to-end alignment workflows while still accessing lower-level functions
for custom pipelines.

At its current stage, ``fMRI-HA`` provides:

* preprocessing utilities for handling fMRI-related neuroimaging files and data preparation,
* searchlight generation tools for both cortical surface data and volumetric data,
* hyperalignment workflows for response-based and connectivity-based analyses,
* common-space construction and transformation utilities,
* statistical and MVPA-related analysis modules,
* GUI for configuring, launching, and monitoring major hyperalignment,
  ISC, IDM, and bsMVPC workflows,
* pipeline configuration and script-generation helpers.

Citation
--------

Please cite the following if you use ``fMRI-HA``:

xxx

.. toctree::
   :maxdepth: 2
   :caption: Contents

   Installation <notebooks/installation>
   Quick Start <notebooks/quick_start>
   Data Preparation <notebooks/data_prep>
   Response Hyperalignment (RHA) <notebooks/rha>
   Connectivity Hyperalignment (CHA) <notebooks/cha>
   Statistical Analysis <notebooks/statistics>
   API References <notebooks/api>
   Understanding Hyperalignment (Optional Reading) <notebooks/understand_ha>

Support
-------------------

If you encounter problems or bugs with ``fMRI-HA``, or have questions or improvement suggestions,
please feel free to get in touch via the `Github issues <https://github.com/SinofWarth/FMRI-HA_TEST/issues>`_.

License information
-------------------

``fMRI-HA`` is distributed under the MIT License.

Please see the `LICENSE <https://github.com/SinofWarth/FMRI-HA_TEST/blob/main/LICENSE>`_
file in the `fMRI-HA` repository for the full license text.
