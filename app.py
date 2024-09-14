from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

import time



# Your blog details

blog_title = "சத்குருவின் பார்வை"

blog_content = "etri nichchayam Idhu vedha sathiyam Kolgai velvadhae Naan konda latchiyam."



# Set up Chrome WebDriver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



try:

    for i in range(1000):  # Loop 1000 times

        try:

            # Open the website

            driver.get("https://www.sece.live/") 



            # Wait for page to load

            time.sleep(0)  # Adjust if necessary depending on the page load speed



            # Navigate to the write page (update this XPath or URL as needed)

            try:

                write_page_link = driver.find_element(By.XPATH, '//a[text()="write"]')  # Adjust the XPath as needed

                write_page_link.click()

            except Exception as e:

                print(f"Write page link not found or could not be clicked: {e}")

                continue  # Skip this iteration and go to the next one



            # Wait for the write page to load

            time.sleep(0)



            # Find and fill the title field

            try:

                title_field = driver.find_element(By.XPATH, '//input[@placeholder="Title (Min 5 characters | Max 70 characters ,)"]')

                title_field.send_keys(blog_title)

            except Exception as e:

                print(f"Title field not found or could not be filled: {e}")

            

            # Find and fill the content field

            try:

                content_field = driver.find_element(By.XPATH, '//textarea[@placeholder="Write something...(Min 10 characters)"]')

                content_field.send_keys(blog_content)

            except Exception as e:

                print(f"Content field not found or could not be filled: {e}")



            # Try submitting the post

            try:

                post_button = driver.find_element(By.XPATH, '//button[text()="Post"]')

                post_button.click()

            except Exception as e:

                print(f"Post button not found or could not be clicked: {e}")



            # Wait to ensure the post is submitted

            time.sleep(0)



            # Optionally, add a small delay between posts to avoid overwhelming the server

            time.sleep(0)



        except Exception as e:

            print(f"An error occurred during iteration {i + 1}: {e}")



finally:

    # Close the browser

    driver.quit()
