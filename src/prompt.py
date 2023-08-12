#List Prompt

#Articles
def prompt_article(text: str) -> str :
    ### This function returns the prompt sent to the API for website article treatment.
    PROMPT_ARTICLE = f"""You work for a web agency specializing in website creation and SEO. The clients send the articles they want to publish text that are audio files transcripted by a speech-to-text model. 
    However this model is not perfect, and sometimes, the generated text is not a ready-to-published text.
    Your role is to modify this text to make it ready to be published on the web.
    The text you need to edit is delimited by triple backticks.

    You remove filling words.
    You segment the text into coherent parts when it is needed.
    You add punctuation where it is needed.
    You proofread and correct the text.
    You explicit the abbreviations.
    You edit key words so that they are in bold.

    The text might contain a Title, subtitles and bullet points, but they are not likely to be explicitly announced. If you recognize a title, a subtitle or a list, edit the text format in consequences.

    Format everything as HTML that can be used in a website. 
    Place the edited text in a <div> element.

    Your answer must be in the same language as the text.

    ```{text}```"""
    return PROMPT_ARTICLE

def prompt_cdc(text: str) -> str :
    ### This function returns the prompt sent to the API for CDC treatment.
    PROMPT_CDC = prompt = f"""General Context : You are working for a web agency that creates websites for small companies and independent worker. 
    One of the department of this company is requested to send a survey to the client collect his preferences for the website to be created.


    Your task :
    You will be provided with a raw text between triple backticks which is the recording of someone reading the survey’s results.

    Perform the following actions :
    - Identify each categories (ie : questions in the survey) and answers from the client
    - Re-write the text with : A title, subtitles (categories) and information corresponding to each category. 
    - Format the text : highlight key words and important information
    - Write a beginning summary with clients information
    - Write a conclusion summary which is 10 percent the length of the initial file, that sums up relevant information for the website creation.

    Format everything as HTML that can be used in a website. 
    Place the edited text in a <div> element.


    Important rules :
    - You must stick to the information provided by the original text.
    - Details such as colors, names and activity are important.
    - Your output must be in French


    Text : ```{text}```"""
    return PROMPT_CDC