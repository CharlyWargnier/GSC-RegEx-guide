import streamlit as st

def main():
    st.header('🔍 GSC RegEx Cheat Sheet', divider='rainbow')

    st.subheader('')
    
    st.markdown("""
    Inspired by [this article from the awesome JC Chouinard](https://www.jcchouinard.com/regex-in-google-search-console/), this cheat sheet harnesses the power of regular expressions to provide insights from your Google Search Console data. This cheat sheet focuses on the Re2 syntax used in GSC, providing a comprehensive set of patterns for different analysis requirements.

    Everyone is welcome to contribute! Feel free to add PRs or suggestions to [this project on GitHub](https://github.com/CharlyWargnier/GSC-RegEx-Guide/blob/main/streamlit_app.py). Your input is greatly appreciated!
    """)

    st.subheader('')
    st.subheader('📚 1. Getting Started: Basic RegEx', divider='blue')
    st.write("**Including Specific Words**")
    st.code(".*seo.*", language='plaintext')
    st.write("**Excluding Patterns**")
    st.code("(Use the custom (regex) filter option under \"Doesn’t match regex\")", language='plaintext')
    st.write("**Pages Path Focus**")
    st.code("^https://www.example.com/(path1|path2|path3)/$", language='plaintext')

    st.subheader('📏 2. Query and URL Length Insights', divider='green')
    st.write("**Short Strings (less than 10 characters)**")
    st.code("^[\w\W\s\S]{1,10}$", language='plaintext')
    st.write("**Extended Queries (over 70 characters)**")
    st.code("^[\w\W\s\S]{70,}$", language='plaintext')
    st.write("**Extensive URLs (beyond 100 characters)**")
    st.code("^[\w\W\s\S]{100,}$", language='plaintext')

    st.subheader('🔗 3. Analyzing URL Structures', divider='orange')
    st.write("**Special Characters Detection**")
    st.code("[^\\/\\.\\-:0-9A-Za-z_]", language='plaintext')
    st.write("**Specific Path Ends (e.g., /jobs/ in Melbourne)**")
    st.code(".*/jobs/.*/melbourne$", language='plaintext')
    st.write("**Final Slash Presence**")
    st.code(".*\\/$", language='plaintext')
    st.write("**Domain Variations**")
    st.code("https?\\:\\/\\/.*example\\.com\\/?$", language='plaintext')

    st.subheader('💡 4. Diving into Query Intent', divider='red')
    st.write("**Information Queries**")
    st.code("who|what|when|how|why", language='plaintext')
    st.write("**Branding Interests**")
    st.code(".*brand.*", language='plaintext')
    st.write("**Commercial Queries**")
    st.code(".*(best|top|vs|review*).*", language='plaintext')
    st.write("**Purchase Intent**")
    st.code(".*(buy|cheap|price|purchase|order).*", language='plaintext')

    st.subheader('🧠 5. Advanced Techniques', divider='violet')
    st.write("**Case Insensitive Matches**")
    st.code("(?i)^(who|what|where|when|why|how)[\" \"]", language='plaintext')
    st.write("**Alerts for Unwanted Content**")
    st.code(".*viagra.*|.*cialis.*|.*levitra.*|.*drugs.*|.*porn.*|.*www.*www.*", language='plaintext')
    st.write("**WordPress Admin Paths**")
    st.code(".*wp-.*", language='plaintext')
    st.write("**Postcode Recognition**")
    st.code(".*-[A-Za-z]{1,2}(\\d{1,2}|\\d[A-Za-z])$", language='plaintext')

if __name__ == "__main__":
    main()
