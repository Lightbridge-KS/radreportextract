import re
from typing import List

class ReportRegexExtractor:
    def extract_hx_imp(self, text) -> str:
        std_type = self.extract_study_type(text)
        hx = self.extract_hx(text, strick=True)
        imp = self.extract_imp(text)
        return "\n\n".join([std_type, hx, imp])
   
    def extract_hx_imp_dict(self, text) -> dict[str, str]:
        return {
            "study_type": self.extract_study_type(text),
            "history": self.extract_hx(text, include_key=False, strick=True),
            "impression": self.extract_imp(text, include_key=False)
        }
        
    @staticmethod
    def extract_study_type(text):
        pattern = r"(.*?)(?=\b(history|indication)\b)"
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            study_type_text = match.group(0).strip() 
            return study_type_text
        else:
            raise ValueError("Study type not match")
        

    
    @staticmethod
    def extract_hx(text, 
                   include_key: bool = True,
                   start_key: List[str] = ["history", "indication"],
                   end_key: List[str] = ["technique", "comparison", "finding", "impression"],
                   strick: bool = True                  
                   ) -> str:
        """
        Extracts the "History" or "Indication" section from the given text.

        This method uses a regex pattern to extract the section starting with any 
        of the `start_key` terms (e.g., "history", "indication") and stops when 
        encountering the next section header defined in `end_key` or upon encountering 
        consecutive newlines/tabs. If `include_key` is False, the matching keyword 
        is removed from the extracted text.

        Args:
            text (str): The report text from which the section is to be extracted.
            include_key (bool): If True, includes the start keyword (e.g., "history") 
                                in the extracted text. Defaults to True.
            start_key (List[str]): List of section keywords to start the extraction. 
                                   Defaults to ["history", "indication"].
            end_key (List[str]): List of section keywords to stop the extraction. 
                                 Defaults to ["technique", "comparison", "finding", "impression"].
            strick (bool): For strick mode, only extract if there is `start_key`; otherwise return "".

        Returns:
            str: The extracted section text. Returns an empty string if no match is found.
        """


        start_key_matched = re.search(f"({'|'.join(start_key)}).*?", text, re.DOTALL | re.IGNORECASE)
        
        end_key = end_key + [x + "s" for x in end_key] # Add "s" (pleural) variant 
        
        if strick or start_key_matched:
            # Strick mode or non-strick mode with start_key
            pattern = fr"(({'|'.join(start_key)}).*?)(?=\b(?:{'|'.join(end_key)})\b|[\n\t]+)"
        else:
            # Non-strick mode without matched start key
            pattern = fr"^(.*)(?=\b(?:{'|'.join(end_key)})\b|[.+$])"
        
        # Extract the "History" or "Indication" section
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        
        if match:
            hx_text = match.group(0).strip()
        else:
            # If no match is found
            return "" 

        # If include_key is False, remove the "history" or "indication" keyword from the result
        if include_key:
            return hx_text
        else:
            key_match = re.search(fr"({"|".join(start_key)}):\s*(.*)", hx_text, re.DOTALL | re.IGNORECASE)
            if key_match:
                hx_text_nokey = key_match.group(2).strip()
                return hx_text_nokey
            else:
                # If the structure is unexpected and no keyword is found, return the original text
                return hx_text

            
    @staticmethod
    def extract_imp(text, include_key: bool = True) -> str:
        # Regular expression to match the "Impression" section until the end
        pattern = r"impression.*"
        # Extract the "Impression" section
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            imp_text = match.group(0).strip()
        else:
            # If no match is found
            return "" 
    
        if include_key:
            return imp_text
        
        # If include_key is False, remove the "impression" keyword from the result
        else:
            key_match = re.search(r"impression:\s*(.*)", imp_text, re.DOTALL | re.IGNORECASE)
            if key_match:
                imp_text_nokey = match.group(1).strip()
                return imp_text_nokey
            else: 
                # If the structure is unexpected and no keyword is found, return the original text
                return imp_text
                