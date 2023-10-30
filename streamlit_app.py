import streamlit as st

st.set_page_config(
    page_title="GSC RegEx Cheat Sheet",
    page_icon="🔍"
)

def main():
    st.header('🔍 GSC RegEx Cheat Sheet', divider='rainbow')

    st.subheader('')
    
    st.markdown("""
    Inspired by [this article from the awesome JC Chouinard](https://www.jcchouinard.com/regex-in-google-search-console/), this cheat sheet harnesses the power of regular expressions to provide insights from your Google Search Console data!

    Everyone is welcome to contribute! Feel free to add PRs or suggestions to [this project on GitHub](https://github.com/CharlyWargnier/GSC-RegEx-Guide/blob/main/streamlit_app.py). Your input is greatly appreciated!
    """)

    st.subheader('')

    st.subheader('📚 1. Getting Started: Basic RegEx', divider='blue')
    st.write("**Including Specific Words**")
    st.write("This pattern matches any string containing 'seo'.")
    st.code(".*seo.*", language='plaintext')

    st.write("**Excluding Patterns**")
    st.write("- Exclude range of characters: `[^abc]` will match any character except `a`, `b`, or `c`.")
    st.code("[^abc]", language='plaintext')
    
    st.write("- Exclude non-word characters common in URLs:")
    st.code("[^\\/\\.\\-\\:]", language='plaintext')
    
    st.write("- Exclude word characters: `[^0-9A-Za-z_]` will match any character that is not a word character.")
    st.code("[^0-9A-Za-z_]", language='plaintext')

    st.write("**Pages Path Focus**")
    st.write("Match specific paths within a domain using regex. For example, the pattern below matches URLs under `path1`, `path2`, or `path3` on `www.example.com`:")
    st.code("^https://www.example.com/(path1|path2|path3)/$", language='plaintext')

    st.subheader('📏 2. Query and URL Length Insights', divider='green')
    st.write("**Short Strings (less than 10 characters)**")
    st.write("Matches strings that are less than 10 characters long.")
    st.code("^[\w\W\s\S]{1,10}$", language='plaintext')
    st.write("**Extended Queries (over 70 characters)**")
    st.write("Matches queries that are more than 70 characters long.")
    st.code("^[\w\W\s\S]{70,}$", language='plaintext')
    st.write("**Extensive URLs (beyond 100 characters)**")
    st.write("Matches URLs that are more than 100 characters long.")
    st.code("^[\w\W\s\S]{100,}$", language='plaintext')

    st.subheader('🔗 3. Analyzing URL Structures', divider='orange')
    st.write("**Special Characters Detection**")
    st.write("This pattern matches URLs containing special characters.")
    st.code("[^\\/\\.\\-:0-9A-Za-z_]", language='plaintext')
    st.write("**Specific Path Ends (e.g., /jobs/ in Melbourne)**")
    st.write("Matches URLs ending with '/jobs/' followed by 'melbourne'.")
    st.code(".*/jobs/.*/melbourne$", language='plaintext')
    st.write("**Final Slash Presence**")
    st.write("Matches URLs ending with a forward slash.")
    st.code(".*\\/$", language='plaintext')
    st.write("**Domain Variations**")
    st.write("Matches variations of 'example.com' with or without 'www' and 'http' or 'https'.")
    st.code("https?\\:\\/\\/.*example\\.com\\/?$", language='plaintext')

    st.subheader('💡 4. Diving into Query Intent', divider='red')
    st.write("**Information Queries**")
    st.write("Matches queries asking questions (who, what, when, how, why).")
    st.code("who|what|when|how|why", language='plaintext')
    st.write("**Branding Interests**")
    st.write("Matches queries containing the word 'brand'.")
    st.code(".*brand.*", language='plaintext')
    st.write("**Commercial Queries**")
    st.write("Matches queries with commercial intent (best, top, vs, review).")
    st.code(".*(best|top|vs|review*).*", language='plaintext')
    st.write("**Purchase Intent**")
    st.write("Matches queries showing purchase intent (buy, cheap, price, purchase, order).")
    st.code(".*(buy|cheap|price|purchase|order).*", language='plaintext')

    st.subheader('🧠 5. Advanced Techniques', divider='violet')
    st.write("**Case Insensitive Matches**")
    st.write("Matches queries regardless of case, asking questions (who, what, where, when, why, how).")
    st.code("(?i)^(who|what|where|when|why|how)[\" \"]", language='plaintext')
    st.write("**Alerts for Unwanted Content**")
    st.write("Matches unwanted content such as drugs, porn, etc.")
    st.code(".*viagra.*|.*cialis.*|.*levitra.*|.*drugs.*|.*porn.*|.*www.*www.*", language='plaintext')
    st.write("**WordPress Admin Paths**")
    st.write("Matches URLs containing 'wp-' which often indicates WordPress admin paths.")
    st.code(".*wp-.*", language='plaintext')
    st.write("**Postcode Recognition**")
    st.write("Matches UK-style postcodes at the end of a string.")
    st.code(".*-[A-Za-z]{1,2}(\\d{1,2}|\\d[A-Za-z])$", language='plaintext')

if __name__ == "__main__":
    main()
