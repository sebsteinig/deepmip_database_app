import streamlit as st

from app_modules import init_sidebar
from deepmip_modules import model_table
from bibliography import init_bibliography

st.set_page_config(
    page_title="Home",
    layout="wide",
)

init_sidebar()

st.write("# Welcome to the DeepMIP-Eocene model database! 👋")

st.markdown(
    """
    The **D**eep **T**ime **M**odel **I**ntercomparison **P**roject (DeepMIP)-Eocene
    is a collaboration of eight climate modelling groups from around the world, 
    each carrying out standardised simulations of the early Eocene climate optimum 
    (EECO, ∼ 50 million years ago). All generated data is freely available to
    everyone. This website provides an overview of the available data and an interface 
    to easily extract point data from all available simulations for a streamlined
    model-data comparison.

    ###  How to Get Started
    Select any of the following pages to start your analysis:

    - <a href='Download_global_model_data' target='_self'>Download global model data</a> from the CEDA Archive.
    - <a href='Extract_local_model_data' target='_self'>Extract local model data</a> for any location, ready to be imported into your spreadsheet.
    - <a href='Plot_local_model_data' target='_self'>Plot local model data</a> (monthly, seasonal, annual) and it's relation to CO$_2$ and global mean temperature.
    - <a href='Map_sites_and_boundary_conditions' target='_self'>Map sites and boundary conditions</a> to see how your sites are represented in different models.
    - <a href='Validation_tables' target='_self'>View the validation tables</a> for an overview of available data an ensemble consistency metrics. 

    """,
    unsafe_allow_html=True,
)

st.subheader("DeepMIP Models")
st.markdown(
    """
    An overview of all participating models and their available simulations is given below.

    """
)
st.dataframe(model_table(), use_container_width=False)


st.markdown(
    """
    ### Want to learn more?
    - DeepMIP experimental design paper: 
    [Lunt et al. (2017)](https://doi.org/10.5194/gmd-10-889-2017)
    - Large-scale climate features in the simulations: 
    [Lunt et al. (2021)](https://doi.org/10.5194/cp-17-203-2021)
    - Overview of the DeepMIP database 
    [in review](https://sebsteinig.github.io/blog/2023/DeepMIP-database-paper/)
    - Official [DeepMIP website](https://www.deepmip.org)
    - Model description papers:
        - CESM1.2-CAM5: [Zhu et al., (2019)](https://doi.org/10.1126/sciadv.aax1874)
        - IPSLCM5A2: [Zhang et al., (2020)](https://doi.org/10.5194/cp-16-1263-2020)
        - all other: [Lunt et al. (2021)](https://doi.org/10.5194/cp-17-203-2021)

    ### Publications
    The DeepMIP model data from this data set have been used in the following publications: 

    """
)

init_bibliography()
