import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Streamlit app title
st.title("Blog Automation Tool")

# User inputs
blog_title = st.text_input("Enter Blog Title", value="தமிழக வெற்றிக் கழகம்")
blog_content = st.text_area("Enter Blog Content", value="வணக்கம் தோழரே...!!தமிழக வெற்றிக் கழகம்தங்களை அன்புடன் வரவேற்கிறது..")
iterations = st.number_input("Number of Times to Run", min_value=1, max_value=1000, value=1, step=1)

# Run button
if st.button("Run Automation"):
    # Set up Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        for i in range(iterations):  # Loop based on user input
            try:
                # Open the website
                driver.get("https://www.sece.live/") 

                # Wait for page to load
                time.sleep(1)  # Adjust if necessary depending on the page load speed

                # Navigate to the write page (update this XPath or URL as needed)
                try:
                    write_page_link = driver.find_element(By.XPATH, '//a[text()="write"]')  # Adjust the XPath as needed
                    write_page_link.click()
                except Exception as e:
                    st.write(f"Write page link not found or could not be clicked: {e}")
                    continue  # Skip this iteration and go to the next one

                # Wait for the write page to load
                time.sleep(1)

                # Find and fill the title field
                try:
                    title_field = driver.find_element(By.XPATH, '//input[@placeholder="Title (Min 5 characters | Max 70 characters ,)"]')
                    title_field.send_keys(blog_title)
                except Exception as e:
                    st.write(f"Title field not found or could not be filled: {e}")
                
                # Find and fill the content field
                try:
                    content_field = driver.find_element(By.XPATH, '//textarea[@placeholder="Write something...(Min 10 characters)"]')
                    content_field.send_keys(blog_content)
                except Exception as e:
                    st.write(f"Content field not found or could not be filled: {e}")

                # Try submitting the post
                try:
                    post_button = driver.find_element(By.XPATH, '//button[text()="Post"]')
                    post_button.click()
                except Exception as e:
                    st.write(f"Post button not found or could not be clicked: {e}")

                # Wait to ensure the post is submitted
                time.sleep(1)

                st.write(f"Iteration {i + 1} completed successfully")

            except Exception as e:
                st.write(f"An error occurred during iteration {i + 1}: {e}")

    finally:
        # Close the browser
        driver.quit()

    st.write("Automation completed.")
