.. image:: _static/fmriha_logo.png
   :alt: fMRI-HA logo
   :width: 200px
   :align: left

fMRI-HA
=======

.. raw:: html

   <div style="clear: both;"></div>

About
-----

``fMRI-HA`` is a Python package designed for flexible hyperalignment analysis of
functional magnetic resonance imaging (fMRI) data. It supports both response
hyperalignment (RHA) and connectivity hyperalignment (CHA), works with multiple
fMRI data formats, and provides tools for whole-brain searchlight analysis,
ROI-level analysis, GUI-based workflows, and statistical evaluation.

This tool allows you to easily do the following:

* **Perform response hyperalignment based on shared stimulus-evoked activity patterns.**

* **Perform connectivity hyperalignment based on individual functional connectivity profiles.**

* **Run whole-brain searchlight hyperalignment across cortical or volumetric fMRI data.**

* **Apply hyperalignment within a specific region of interest for focused ROI-level analysis.**

* **Process multiple fMRI data formats, including CIFTI, GIFTI, and NIFTI.**

* **Complete the full hyperalignment pipeline through an interactive GUI workflow.**

* **Calculate statistical metrics to evaluate and compare hyperalignment performance.**

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

Support
-------------------

If you encounter problems or bugs with ``fMRI-HA``, or have questions or improvement suggestions,
please feel free to get in touch via the `Github issues <https://github.com/SinofWarth/GonglabHyperAligement/issues>`_.

License information
-------------------

``fMRI-HA`` is distributed under the BSD 3-Clause "New" or "Revised" License.

Please see the LICENSE file in the ``fMRI-HA`` repository for the full license text.
