from typing import TypedDict
from dataclasses import dataclass, field, asdict

@dataclass
class ExampleReport:
    report_text: str
    truth_study_type: str
    truth_hx_w_key: str
    truth_imp_w_key: str


example_report = {}

example_report["MRI_Brain"] = {
    # Study, History, Technique, Comparison
    "study_hx_tech_comp": ExampleReport(
        
        report_text="""
MRI OF THE BRAIN AND ORBITS 

History: MALT lymphoma at the right orbit S/P chemotherapy was sent to follow-up. 

Technique: 
Sagittal SE T1W 
3D FSE FLAIR FS +Gd with MPR 

Comparison: Limited comparison to the MRI brain on 4-6-2022 

Findings: 
There has been markedly decreased size of enhancing lesion at the right orbit, leaving small enhancing lesion at superior and medial intraconal space and superior rectus muscle, abutting right globe without invasion. Complete resolution of lesion at the left orbit.

Impression:    
- Markedly decreased size of enhancing lesion at the right orbit, leaving small aenhancing lesion at superior and medial intraconal space and superior rectus muscle, abutting right globe without invasion. Findings are suspicion for residual tumor. 
- Complete resolution of lesion at the left orbit
""",
        truth_study_type = "MRI OF THE BRAIN AND ORBITS",
        truth_hx_w_key = "History: MALT lymphoma at the right orbit S/P chemotherapy was sent to follow-up.",
        truth_imp_w_key = """
Impression:    
- Markedly decreased size of enhancing lesion at the right orbit, leaving small aenhancing lesion at superior and medial intraconal space and superior rectus muscle, abutting right globe without invasion. Findings are suspicion for residual tumor. 
- Complete resolution of lesion at the left orbit
"""
    ),
    # Study, History, \n, then Technique (no key)
    "study_hx_newline": ExampleReport(
        report_text="""
MRI OF THE BRAIN AND ORBITS 

History: MALT lymphoma at the right orbit S/P chemotherapy was sent to follow-up. 

Sagittal SE T1W 
""",
        truth_study_type = "MRI OF THE BRAIN AND ORBITS",
        truth_hx_w_key = "History: MALT lymphoma at the right orbit S/P chemotherapy was sent to follow-up.",
        truth_imp_w_key = ""
    ),
    # Study, History, Technique (using tab)
    "study_hx_tech_tab": ExampleReport(
        report_text="""
MDCT OF THE NECK   Indication: A 58-year-old man, known case of nasopharyngeal cancer (T4N2M1) with lung metastasis   Technique: Post contrast enhanced axial scan of the neck using 1.0 mm slice thickness with 3.0 mm axial, coronal and sagittal reformation   Comparison: The prior CT of the neck taken on October 4, 2015   Findings:  	The current study reveals slight shrinkage but no significant change in extension of the preexisting ill-defined hypodense lesion with partial mild enhancement in some portions, epicenter at the left-sided nasopharynx. Extension of the lesion is described as follow;  ... Superior: No interval change of extension into the left foramen Ovale and left inferior orbital fissure. No significant change of few enhancing foci in the left inferior temporal lobe.  ... Anterior: Involvement of the left infratemporal fossa, left PPF, left retroantral space, and left masticator space. Erosion and sclerotic change of the left pterygoid bone and posterior wall of the left maxillary sinus, unchanged.
""",
        truth_study_type = "MDCT OF THE NECK",
        truth_hx_w_key = "Indication: A 58-year-old man, known case of nasopharyngeal cancer (T4N2M1) with lung metastasis",
        truth_imp_w_key = ""
    ),
    # Study, History, Technique (using tab) --- No Next Section KeyWord
    "study_hx_tech_tab_nokey": ExampleReport(
        report_text="""
Indications: A 58-year-old man, known case of nasopharyngeal cancer (T4N2M1).
""",
        truth_study_type = "MDCT OF THE NECK",
        truth_hx_w_key = "Indications: A 58-year-old man, known case of nasopharyngeal cancer (T4N2M1).",
        truth_imp_w_key = ""
    )
}




if __name__ == "__main__":
    pass
    
