import pytest
from dataclasses import dataclass, field, asdict

from radreportextract import ReportRegexExtractor
from test.example_report import example_report

def report_to_list_tuple(study: str, lhs, rhs):
    "Generate list of tuples from `example_report`"
    dict_k_v = dict(zip([asdict(v)[lhs] for k, v in example_report[study].items()],
                        [asdict(v)[rhs] for k, v in example_report[study].items()]))
    
    return list(dict_k_v.items())



class TestReportRegexExtractor:
    "Test for `ReportRegexExtractor`"
    @pytest.fixture
    def extractor(self):
        return ReportRegexExtractor()
    
    def first_test(self):
        assert 1+1 == 2
    
    # Test Extract History with Keys
    @pytest.mark.parametrize(
        "report_text, expected", 
        # Generate List of Tuple with `report_text` and `truth_hx_w_key` values
        report_to_list_tuple("MRI_Brain", "report_text", "truth_hx_w_key")
    )
    def test_extract_hx_with_key(self, extractor, report_text, expected):
        """Test extract history with keys from MRI Brain
        """
        assert extractor.extract_hx(report_text).strip() == expected.strip()
    
     # Test Extract Impression with Keys
    @pytest.mark.parametrize(
        "report_text, expected", 
        report_to_list_tuple("MRI_Brain", "report_text", "truth_imp_w_key")
    )
    def test_extract_imp_with_key(self, extractor, report_text, expected):
        """Test extract impression with keys from MRI Brain
        """
        assert extractor.extract_imp(report_text).strip() == expected.strip()