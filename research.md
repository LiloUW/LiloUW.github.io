---
layout: research
title: "Research"
permalink: /research/
---

### Research Spotlight: Science Jubilee

<div class="row g-4 mb-4 align-items-center">
  <div class="col-md-7" markdown="1">
In the Pozzo Group we are developing open hardware and open software for self-driving labs using low-cost and accessible automation. Science Jubilee is an open-science, multi-tool motion platform for science automation, developed in collaboration with Dr. Nadya Peek and her group.

The video shows our autonomous color matching demo, using Science Jubilee equipped with a Raspberry Pi camera and an Opentrons OT-2 pipette.

Learn more: [Documentation](https://science-jubilee.readthedocs.io/en/latest/index.html) | [GitHub](https://github.com/machineagency/science_jubilee) | [Paper in *Digital Discovery*](https://pubs.rsc.org/en/content/articlelanding/2023/dd/d3dd00105a)
  </div>
  <div class="col-md-5">
    <video controls muted playsinline preload="metadata" poster="{{ '/assets/img/research/science-jubilee.jpg' | relative_url }}" class="rounded w-100">
      <source src="{{ '/assets/video/jubilee-color-match-demo.mp4' | relative_url }}" type="video/mp4">
      <img src="{{ '/assets/img/research/science-jubilee.jpg' | relative_url }}" alt="Science Jubilee platform" class="img-fluid rounded">
    </video>
    <p class="text-muted small mt-2">Autonomous color matching demo with Science Jubilee</p>
  </div>
</div>

### Laboratory Facilities

- **Small-angle X-ray scattering (SAXS):** our Xenocs Xeuss 3.0, equipped with both copper and molybdenum sources, allows high-throughput SAXS experiments on solids, liquids, and gels. Optional stages allow measurements from -196 °C to 350 °C, under humid and atmospheric environments, and under tensile and shear forces. The Pozzo group manages the SAXS for MEM-C, open for campus-wide use at UW.
- **High-throughput robotics:** Opentrons-based liquid handling robots are our workhorse for high-throughput synthesis. Our custom Python scripts for making samples and designing new hardware are open source on [GitHub](https://github.com/pozzo-research-group/OT2-DOE). We also use Science Jubilee, a modular platform for materials exploration, creation, and sonication thanks to its tool-changing capabilities.
- **PhasIR:** an open-source thermal analysis tool built by our group to measure melting, boiling, and phase transition temperatures in a high-throughput manner. It uses an infrared thermal camera to match the accuracy of conventional DSC instruments at a total cost of around $1000.
- **HARDy:** a Python package, developed as part of a capstone project for the DIRECT program, that increases the data density of images through numerical and RGB transformations to improve classification with convolutional neural networks. [GitHub](https://github.com/EISy-as-Py/hardy)
- **Functional data analysis:** tools based on the functional data analysis (FDA) framework to process high-throughput data from SAXS, spectroscopy, and other sources, for building faithful and generalizable materials acceleration platforms.

We also use shared facilities as members of the Molecular Analysis Facility (MAF), the NSF MRSEC Molecular Engineering Materials Center (MEM-C), the Clean Energy Institute (CEI), the Washington Clean Energy Testbeds (WCET), the Center for the Science of Synthesis Across Scales (CSSAS), and the Research Training Testbeds (RTT). We collaborate extensively with national user facilities, including the NIST Center for Neutron Research (NCNR), the Advanced Photon Source at Argonne National Laboratory, and the Stanford Synchrotron Radiation Lightsource (SSRL).

### From Lab to Market

Technologies developed in our laboratory have led to multiple startup companies:

- **JanuTech** (2025 – present): nanostructured additives for performance improvement in fast-charging lithium and sodium-ion batteries.
- **Membrion Inc.** (2015 – present): nanoporous ceramic membranes for efficient ion separations and industrial process water purification via electrodialysis.
- **PolyDrop LLC** (2013 – 2023): conductive polymer additives for electrostatic charge dissipation in coatings and rubber materials.

### Hurricane Maria Energy & Health Project

In 2017, following Hurricane Maria's devastation of Puerto Rico, our team launched a research and humanitarian initiative in Jayuya, studying health impacts of extended power outages on rural patients dependent on electricity for medical treatments. We deployed 21 solar nanogrid installations and published peer-reviewed research on small-scale clean energy systems for emergency applications. This work was featured in *The New York Times* and other major publications.

<div class="row g-3 mt-1">
  <div class="col-md-6">
    <img src="{{ '/assets/img/research/hurricane-maria.jpg' | relative_url }}" alt="Installing a solar panel in Jayuya, Puerto Rico" class="research-image rounded">
  </div>
  <div class="col-md-6">
    <img src="{{ '/assets/img/research/hurricane-maria-team.jpg' | relative_url }}" alt="Prof. Pozzo assembling a solar nanogrid on a roof, and the team on a rooftop in Jayuya" class="research-image rounded">
  </div>
</div>
