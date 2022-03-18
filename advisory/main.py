import pyautogui as pag
import time
import pyperclip

title = "80 billion riyals, the volume of spending on domestic overnight trips in the Kingdom during 2021"
article = """80 billion riyals, the volume of spending on domestic overnight trips in the Kingdom during 2021

Al Eqtesadiah news reported, the Minister of Tourism confirmed that the volume of spending on local overnight trips in the Kingdom grew by 30% from 2019, to reach 80 billion riyals during 2021, as the number of local overnight trips reached 60 million trips, an increase of 25% from 2019.

Ahmed Al-Khatib said, through his account on “Twitter”, that the Saudi tourism sector witnessed many achievements in 2021, despite the challenges associated with the pandemic. He added, “The Crown Prince set clear goals for the tourism sector by 2030 and provided us with the capabilities, and we still have to achieve the goals.”

And he indicated that the recovery rate in the number of incoming trips to the Kingdom during 2021 (other than Hajj and Umrah) amounted to 76%, although the global recovery amounted to 24% from 2019 levels, while stressing that the growth rate of the number of workers in the Saudi tourism sector increased by 10% during 2021 compared to the year 2020.

The Minister of Tourism indicated that the Kingdom's most important tourism achievements in the past year were the Crown Prince's announcement of the establishment of the Global Center for Tourism Sustainability, the Kingdom's winning of the seat of the first vice president in the Executive Council of the Tourism Organization, the selection of the Kingdom to host the World Travel and Tourism Summit 2022, the establishment of the World Tourism Academy, and the launch of the office Regional Tourism Organization in the Kingdom.

Ahmed Al-Khatib added, "We aim to reach 10% of tourism's GDP contribution in 2030, receive 100 million visits annually, and add one million jobs."""
footer = """

<h2>More News</h2>

<ul>
    <li>
        <a
            href="https://advisory-corp.com/saudi-arabia-is-among-the-top-pioneering-nations/"
            rel="noopener"
            target="_blank"
            >Saudi Arabia Is Among The Top Pioneering, Innovative Nations In
            Providing Government Services</a
        >
    </li>
</ul>

<h2>Our Services</h2>
<ul>
    <li>
        <a
            href="https://advisory-corp.com/feasibility-studies/"
            rel="noopener"
            target="_blank"
            >Innovation Strategy & Feasibility Studies</a
        >
    </li>
    <li>
        <a
            href="https://advisory-corp.com/real-estate-advisory/"
            rel="noopener"
            target="_blank"
            >Real Estate Advisory</a
        >
    </li>
    <li>
        <a
            href="https://advisory-corp.com/corporate-finance-business-valuation/"
            rel="noopener"
            target="_blank"
            >Business Valuation</a
        >
    </li>
    <li>
        <a href="https://advisory-corp.com/" rel="noopener" target="_blank"
            >Advisory-Corp | Leading Consulting and Financial Advisory Group</a
        >
    </li>
</ul>"""


x, y = pag.locateCenterOnScreen("addNewPost.PNG")

pag.click(x, y + 180)
# pag.write(title, interval=0.01)
pyperclip.copy(title)
pag.hotkey("ctrl", "v")
pag.click(x, y + 400)
# pag.write(article, interval=0.01)
# pag.write(footer, interval=0.01)
pyperclip.copy(article + footer)
pag.hotkey("ctrl", "v")

pag.click(pag.locateCenterOnScreen("categoryNews.PNG"))
pag.press("pagedown", presses=10, interval=0.05)

x, y = pag.locateCenterOnScreen("titleColour.PNG")
pag.click(x + 400, y)
pag.moveRel(90, 0)
pag.click()
pag.write("#fff")
