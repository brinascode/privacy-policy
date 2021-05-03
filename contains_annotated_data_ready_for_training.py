import spacy
import random


TRAIN_DATA = [("We collect the content, communications and other information you provide when you use our Products, including when you sign up for an account, create or share content, and message or communicate with others. This can include information in or about the content you provide (like metadata), such as the location of a photo or the date a file was created. It can also include what you see through features we provide, such as our camera, so we can do things like suggest masks and filters that you might like, or give you tips on using camera formats. Our systems automatically process content and communications you and others provide to analyze context and what's in them", {'entities': [(374, 434, 'Identification'), (302, 321, 'Location')]}), ('We collect information about the people, Pages, accounts, hashtags and groups you are connected to and how you interact with them across our Products, such as people you communicate with the most or groups you are part of. We also collect contact information if you choose to upload, sync or import it from a device (such as an address book or call log or SMS log history), which we use for things like helping you and others find people you may know and for the other purposes listed below.', {'entities': [(151, 221, 'Habits and Behavior')]}), ("Your usage. We collect information about how you use our Products, such as the types of content you view or engage with; the features you use; the actions you take; the people or accounts you interact with; and the time, frequency and duration of your activities. For example, we log when you're using and have last used our Products, and what posts, videos and other content you view on our Products. We also collect information about how you use features like our camera.", {'entities': [(211, 262, 'Tracking'), (165, 205, 'Habits and Behavior'), (143, 163, 'Habits and Behavior'), (121, 141, 'Habits and Behavior'), (75, 119, 'Habits and Behavior')]}), ('Things others do and information they provide about you. We also receive and analyze content, communications and information that other people provide when they use our Products. This can include information about you, such as when others share or comment on a photo of you, send a message to you, or upload, sync or import your contact information.', {'entities': [(317, 348, 'Identification'), (227, 273, 'Identification'), (125, 150, 'Identification')]}), ('Device attributes: information such as the operating system, hardware and software versions, battery level, signal strength, available storage space, browser type, app and file names and types, and plugins.', {'entities': [(164, 192, 'Personal metadata')]}), ('Device operations: information about operations and behaviors performed on the device, such as whether a window is foregrounded or backgrounded, or mouse movements (which can help distinguish humans from bots).', {'entities': [(148, 163, 'Tracking'), (19, 85, 'Tracking')]}), ('Identifiers: unique identifiers, device IDs, and other identifiers, such as from games, apps or accounts you use, and Family Device IDs (or other identifiers unique to Facebook Company Products associated with the same device or account).', {'entities': [(13, 31, 'Identification')]}), ('Device signals: Bluetooth signals, and information about nearby Wi-Fi access points, beacons, and cell towers.', {'entities': [(39, 109, 'Identification'), (16, 33, 'Identification')]}), ('Data from device settings: information you allow us to receive through device settings you turn on, such as access to your GPS location, camera or photos.', {'entities': [(137, 153, 'Location'), (100, 135, 'Location')]}), ('Network and connections: information such as the name of your mobile operator or ISP, language, time zone, mobile phone number, IP address, connection speed and, in some cases, information about other devices that are nearby or on your network, so we can do things like help you stream a video from your phone to your TV.', {'entities': [(107, 126, 'Identification')]}), ('Cookie data: data from cookies stored on your device, including cookie IDs and settings. Learn more about how we use cookies in the Facebook Cookies Policy and Instagram Cookies Policy.', {'entities': [(13, 52, 'Tracking')]}), ('Advertisers, app developers, and publishers can send us information through Facebook Business Tools they use, including our social plug-ins (such as the Like button), Facebook Login, our APIs and SDKs, or the Facebook pixel. These partners provide information about your activities off Facebook—including information about your device, websites you visit, purchases you make, the ads you see, and how you use their services—whether or not you have a Facebook account or are logged into Facebook. For example, a game developer could use our API to tell us what games you play, or a business could tell us about a purchase you made in its store. We also receive information about your online and offline actions and purchases from third-party data providers who have the rights to provide us with your information.', {'entities': [(336, 414, 'Third-party'), (260, 285, 'Third-party'), (231, 239, 'Third-party')]}), ("We use location-related information-such as your current location, where you live, the places you like to go, and the businesses and people you're near-to provide, personalize and improve our Products, including ads, for you and others. Location-related information can be based on things like precise device location (if you've allowed us to collect it), IP addresses, and information from your and others' use of Facebook Products (such as check-ins or events you attend).", {'entities': [(118, 151, 'Location'), (83, 108, 'Location'), (67, 81, 'Location'), (44, 65, 'Location')]}), ('If you have it turned on, we use face recognition technology to recognize you in photos, videos and camera experiences.', {'entities': [(26, 87, 'Identification')]}), ('We use the information we have about you-including information about your interests, actions and connections-to select and personalize ads, offers and other sponsored content that we show you. Learn more about how we select and personalize ads, and your choices over the data we use to select ads and other sponsored content for you in the Facebook Settings and Instagram Settings.', {'entities': [(85, 138, 'Habits and Behavior'), (51, 83, 'Habits and Behavior')]}), ('If the ownership or control of all or part of our Products or their assets changes, we may transfer your information to the new owner.', {'entities': [(0, 134, 'Personal metadata')]}), ('Networks and connections. We collect information about the people, Pages, accounts, hashtags and groups you are connected to and how you interact with them across our Products, such as people you communicate with the most or groups you are part of. We also collect contact information if you choose to upload, sync or import it from a device (such as an address book or call log or SMS log history), which we use for things like helping you and others find people you may know and for the other purposes listed below.', {'entities': [(343, 397, 'Personal metadata'), (177, 247, 'Habits and Behavior')]}), ("Your usage. We collect information about how you use our Products, such as the types of content you view or engage with; the features you use; the actions you take; the people or accounts you interact with; and the time, frequency and duration of your activities. For example, we log when you're using and have last used our Products, and what posts, videos and other content you view on our Products. We also collect information about how you use features like our camera.", {'entities': [(339, 400, 'Tracking'), (284, 333, 'Tracking'), (211, 262, 'Tracking'), (165, 205, 'Habits and Behavior'), (143, 163, 'Tracking'), (121, 141, 'Habits and Behavior'), (75, 119, 'Habits and Behavior'), (23, 65, 'Habits and Behavior')]}), ('Things others do and information they provide about you. We also receive and analyze content, communications and information that other people provide when they use our Products. This can include information about you, such as when others share or comment on a photo of you, send a message to you, or upload, sync or import your contact information.', {'entities': [(275, 296, 'Identification'), (227, 273, 'Identification'), (0, 55, 'Identification')]}), ('Device attributes: information such as the operating system, hardware and software versions, battery level, signal strength, available storage space, browser type, app and file names and types, and plugins.', {'entities': [(164, 192, 'Tracking')]}), ('Device operations: information about operations and behaviors performed on the device, such as whether a window is foregrounded or backgrounded, or mouse movements (which can help distinguish humans from bots).', {'entities': [(148, 163, 'Tracking'), (19, 85, 'Tracking')]}), ('Device signals: Bluetooth signals, and information about nearby Wi-Fi access points, beacons, and cell towers.', {'entities': [(39, 83, 'Location'), (16, 33, 'Location')]}), ('Data from device settings: information you allow us to receive through device settings you turn on, such as access to your GPS location, camera or photos.', {'entities': [(147, 153, 'Identification'), (137, 143, 'Identification'), (123, 126, 'Location')]}), ('Network and connections: information such as the name of your mobile operator or ISP, language, time zone, mobile phone number, IP address, connection speed and, in some cases, information about other devices that are nearby or on your network, so we can do things like help you stream a video from your phone to your TV.', {'entities': [(218, 243, 'Location'), (107, 126, 'Identification')]}), ('Cookie data: data from cookies stored on your device, including cookie IDs and settings. Learn more about how we use cookies in the Facebook Cookies Policy and Instagram Cookies Policy.', {'entities': [(13, 52, 'Tracking')]}), ('These partners provide information about your activities off Facebook—including information about your device, websites you visit, purchases you make, the ads you see, and how you use their services—whether or not you have a Facebook account or are logged into Facebook.', {'entities': [(172, 198, 'Habits and Behavior'), (151, 166, 'Habits and Behavior'), (131, 149, 'Habits and Behavior'), (111, 129, 'Tracking'), (41, 69, 'Identification'), (0, 34, 'Third-party')]}), ('Of course, you’ll also provide us whatever information you send through our services, such as Snaps and Chats.', {'entities': [(11, 84, 'Personal metadata')]}), ('how you interact with our services, such as which filters you view or apply to Snaps, which Stories you watch on Discover, whether you’re using Spectacles, or which search queries you submit.', {'entities': [(159, 190, 'Tracking'), (44, 75, 'Identification')]}), ('how you communicate with other Snapchatters, such as their names, the time and date of your communications, the number of messages you exchange with your friends, which friends you exchange messages with the most, and your interactions with messages (such as when you open a message or capture a screenshot).', {
    'entities': [(163, 212, 'Identification'), (108, 161, 'Tracking'), (66, 106, 'Tracking'), (0, 30, 'Habits and Behavior')]}), ('information about your hardware and software, such as the hardware model, operating system version, device memory, advertising identifiers, unique application identifiers, apps installed, unique device identifiers, browser type, language, battery level, and time zone;', {'entities': [(172, 186, 'Tracking')]}), ('information from device sensors, such as accelerometers, gyroscopes, compasses, microphones, and whether you have headphones connected; and', {'entities': [(97, 134, 'Tracking'), (41, 55, 'Tracking')]}), ('Device Phonebook. Because Snapchat is all about communicating with friends, we may—with your permission—collect information from your device’s phonebook.', {'entities': [(143, 152, 'Identification')]}), ('Camera and Photos. Many of our services require us to collect images and other information from your device’s camera and photos. For example, you won’t be able to send Snaps or upload photos from your camera roll unless we can access your camera or photos.', {'entities': [(201, 212, 'Identification'), (54, 127, 'Identification'), (0, 17, 'Identification')]}), ('Location Information. When you use our services we may collect information about your location. With your permission, we may also collect information about your precise location using methods that include GPS, wireless networks, cell towers, Wi-Fi access points, and other sensors, such as gyroscopes, accelerometers, and compasses.', {'entities': [(322, 331, 'Location'), (290, 300, 'Tracking'), (242, 261, 'Location'), (210, 227, 'Location'), (205, 208, 'Identification'), (161, 177, 'Identification')]}), ('Information Collected by Cookies and Other Technologies. Like most online services and mobile applications, we may use cookies and other technologies, such as web beacons, web storage, and unique advertising identifiers, to collect information about your activity, browser, and device. We may also use these technologies to collect information when you interact with services we offer through one of our partners, such as advertising and commerce features.', {'entities': [(344, 375, 'Tracking'), (189, 219, 'Habits and Behavior')]}), ('identifiers associated with cookies or other technologies that may uniquely identify your device or browser; and', {'entities': [(0, 35, 'Tracking')]}), ('We require information about your signup and current location, which we get from signals such as your IP address or device settings, to securely and reliably set up and maintain your account and to provide our services to you.', {'entities': [(34, 61, 'Location')]}), ('Subject to your settings, we may collect, use, and store additional information about your location - such as your current precise position or places where you’ve previously used Twitter - to operate or personalize our services including with more relevant content like local trends, stories, ads, and suggestions for people to follow.', {'entities': [(143, 178, 'Tracking'), (115, 139, 'Location')]}), ('In order to operate our services, we keep track of how you interact with links across our services. This includes links in emails we send you and links in Tweets that appear on other websites or mobile applications.', {'entities': [(51, 67, 'Habits and Behavior')]}), ('If you click on an external link or ad on our services, that advertiser or website operator might figure out that you came from Twitter or Periscope, along with other information associated with the ad you clicked such as characteristics of the audience it was intended to reach. They may also collect other personal data from you, such as cookie identifiers or your IP address.', {'entities': [(367, 377, 'Identification'), (340, 358, 'Identification'), (308, 330, 'Identification'), (92, 127, 'Tracking')]}), ('When your browser or device allows it, we use both session cookies and persistent cookies to better understand how you interact with our services, to monitor aggregate usage patterns, and to personalize and otherwise operate our services such as by providing account security,', {'entities': [(111, 127, 'Habits and Behavior')]}), ('We use information you provide to us and data we receive, including Log Data and data from third parties, to make inferences like what topics you may be interested in, how old you are, and what languages you speak. This helps us better promote', {'entities': [(189, 213, 'Identification'), (168, 183, 'Identification'), (130, 166, 'Habits and Behavior')]}), ('Subject to your settings, we may also associate your account with browsers or devices other than those you use to log into Twitter (or associate your logged-out device or browser with other browsers or devices). When you provide other information to Twitter, including an email address, we associate that information with your Twitter account. Subject to your settings, we may also use this information in order to infer other information about your identity, for example by associating your account with hashes of email addresses that share common components with the email address you have provided to Twitter. We do this to operate and personalize our services. For example, if you visit websites with sports content on your laptop, we may show you sports-related ads on Twitter for Android and, if the email address associated with your account shares components with another email address, such as shared first name, last name, or initials, we may later match advertisements to you from advertisers that were trying to reach email addresses containing those components.', {'entities': [(500, 611, 'Tracking'), (475, 499, 'Identification'), (415, 458, 'Identification'), (38, 65, 'Identification')]}), ('Notwithstanding anything to the contrary in this Privacy Policy or controls we may otherwise offer to you, we may preserve, use, share, or disclose your personal data or other safety data if we believe that it is reasonably necessary to comply with a law, regulation, legal process, or governmental request; to protect the safety of any person; to protect the safety or integrity of our platform, including to help prevent spam, abuse, or malicious actors on our services, or to explain why we have removed content or accounts from our services8; to address fraud, security, or technical issues; or to protect our rights or property or the rights or property of those who use our services. However, nothing in this Privacy Policy is intended to limit any legal defenses or objections that you may have to a third par', {'entities': [(755, 769, 'Identification'), (114, 187, 'Personal metadata')]}), ('In the event that we are involved in a bankruptcy, merger, acquisition, reorganization, or sale of assets, your personal data may be sold or transferred as part of that transaction.', {'entities': [(107, 152, 'Personal metadata')]}), ('You can use the contact upload feature and provide us, if permitted by applicable laws, with the phone numbers in your address book on a regular basis, including those of users of our Services and your other contacts. If any of your contacts aren’t yet using our Services, we’ll manage this information for you in a way that ensures those contacts cannot be identified by us', {'entities': [(97, 131, 'Device')]}), ('Usage And Log Information. We collect information about your activity on our Services, like service-related, diagnostic, and performance information. This includes information about your activity (including how you use our Services, your Services settings, how you interact with others using our Services (including when you interact with a business), and the time, frequency, and duration of your activities and interactions), log files, and diagnostic, crash, website, and performance logs and reports. This also includes information about when you registered to use our Services; the features you use like our messaging, calling, Status, groups (including group name, group picture, group description), payments or business features; profile photo, "about" information; whether you are online, when you last used our Services (your "last seen"); and when you last updated your "about" information. copies of your messages', {'entities': [(381, 408, 'Tracking'), (366, 375, 'Habits and Behavior'), (360, 364, 'Tracking')]}), ('Device And Connection Information. We collect device and connection-specific information when you install, access, or use our Services. This includes information such as hardware model, operating system information, battery level, signal strength, app version, browser information, mobile network, connection information (including phone number, mobile operator or ISP), language and time zone, IP address, device operations information, and identifiers (including identifiers unique to Facebook Company Products associated with the same device or account).', {'entities': [(442, 453, 'Identification')]}), ('Location Information. We collect and use precise location information from your device with your permission when you choose to use location-related features, like when you decide to share your location with your contacts or view locations nearby or locations others have shared with you. There are certain settings relating to location-related information which you can find in your device settings or the in-app settings, such as location sharing. Even if you do not use our location-related features, we use IP addresses and other information like phone number area codes to estimate your general location (e.g., city and country). We also use your location information for diagnostics and troubleshooting purposes.', {'entities': [(550, 573, 'Location')]}), ('We receive information about you from other users. For example, when other users you know use our Services, they may provide your phone number, name, and other information (like information from their mobile address book) just as you may provide theirs. They may also send you messages, send messages to groups to which you belong, or call you. We require each of these users to have lawful rights to collect, use, and share your information before providing any information to us.', {'entities': [(23, 49, 'Identification')]}), ('We work with third-party service providers and other Facebook Companies to help us operate, provide, improve, understand, customize, support, and market our Services. For example, we work with them to distribute our apps; provide our technical and physical infrastructure, delivery, and other systems; provide engineering support, cybersecurity support, and operational support; supply location, map, and places information; process payments; help us understand how people use our Services; market our Services; help you connect with businesses using our Services; conduct surveys and research for us; ensure safety, security and integrity; and help with customer service. These companies may provide us with information about you in certain circumstances; for example, app stores may provide us with reports to help us diagnose and fix service issues.', {'entities': [(709, 730, 'Identification')]})]

TEST_DATA = "You give other data to us, such as by syncing your address book or calendar. such as when you fill out a form, (e.g., with demographic data or salary), respond to a survey, or submit a resume or fill out a job application on our Services. If you opt to import your address book, we receive your contacts (including contact information your service provider(s) or app automatically added to your address book when you communicated with addresses or numbers not already in your list). If you sync your contacts or calendars with our Services, we will collect your address book and calendar meeting information to keep growing your network by suggesting connections for you and others, and by providing information about events, e.g. times, places, attendees and contacts. You and others may post content that includes information about you (as part of articles, posts, comments, videos) on our Services. We also may collect public information about you, such as professional-related news and accomplishments, and make it available as part of our Services, including, as permitted by your settings, in notifications to others of mentions in the news. We receive personal data (including contact information) about you when others import or sync their contacts or calendar with our Services, associate their contacts with Member profiles, scan and upload business cards, or send messages using our Services (including invites or connection requests). If you or others opt-in to sync email accounts with our Services, we will also collect “email header” information that we can associate with Member profiles. We receive data about you when you use some of the other services provided by us or our affiliates, including Microsoft. For example, you may choose to send us information about your contacts in Microsoft apps and services, such as Outlook, for improved professional networking activities on our ServicesWe log your visits and use of our Services, including mobile apps. We log usage data when you visit or otherwise use our Services, including our sites, app and platform technology, such as when you view or click on content (e.g., learning video) or ads (on or off our sites and apps), perform a search, install or update one of our mobile apps, share articles or apply for jobs. We use log-ins, cookies, device information and internet protocol (“IP”) addresses to identify you and log your use. As further described in our Cookie Policy, we use cookies and similar technologies (e.g., pixels and ad tags) to collect data (e.g., device IDs) to recognize you and your device(s) on, off and across different services and devices where you have engaged with our Services. We also allow some others to use cookies as described in our Cookie Policy. If you are outside the Designated Countries, we also collect (or rely on others who collect) information about your device where you have not engaged with our Services (e.g., ad ID, IP address, operating system and browser information) so we can provide our Members with relevant ads and better understand their effectiveness. Learn more. You can opt out from our use of data from cookies and similar technologies that track your behavior on the sites of others for ad targeting and other ad-related purposes. For Visitors, the controls are here. When you visit or leave our Services (including some plugins and our cookies or similar technology on the sites of others), we receive the URL of both the site you came from and the one you go to and the time of your visit. We also get information about your network and device (e.g., IP address, proxy server, operating system, web browser and add-ons, device identifier and features, cookie IDs and/or ISP, or your mobile carrier). If you use our Services from a mobile device, that device will send us data about your location based on your phone settings. We will ask you to opt-in before we use GPS or other tools to identify your precise location.We collect information about you when you send, receive, or engage with messages in connection with our Services. For example, if you get a LinkedIn connection request, we track whether you have acted on it and will send you reminders. We also use automatic scanning technology on messages to support and protect our site. For example, we use this technology to suggest possible responses to messages and to manage or block content that violates our User Agreement or Professional Community Policies from our Services. Others buying our Services for your use, such as your employer or your school, provide us with personal data about you and your eligibility to use the Services that they purchase for use by their workers, students or alumni. For example, we will get contact information for “Company Page” administrators and for authorizing users of our premium Services, such as our recruiting, sales or learning products. We receive information about your visits and interaction with services provided by others when you log-in with LinkedIn or visit others’ services that include some of our plugins (such as “Apply with LinkedIn”) or our ads, cookies or similar technologies. This includes your posts and comments including saved drafts, videos you broadcast via RPAN, your messages with other users (e.g., private messages, chats, and modmail), and your reports and other communications with moderators and with us. Your content may include text, links, images, gifs, and videos. For example, we may collect information when you fill out a form, participate in Reddit-sponsored activities or promotions, apply for a job, request customer support, or otherwise communicate with us. We may log information when you access and use the Services. This may include your IP address, user-agent string, browser type, operating system, referral URLs, device information (e.g., device IDs), device settings, pages visited, links clicked, the requested URL, and search terms. Except for the IP address used to create your account, Reddit will delete any IP addresses collected after 100 days. We may receive information from cookies, which are pieces of data your browser stores and sends back to us when making requests, and similar technologies. We use this information to improve your experience, understand user activity, personalize content and advertisements, and improve the quality of our Services. For example, we store and retrieve information about your preferred language and other settings. See our Cookie Notice for more information about how Reddit uses cookies. For more information on how you can disable cookies, please see “Your Choices” below. We may receive and process information about your location. For example, with your consent, we may collect information about the specific location of your mobile device (for example, by using GPS or Bluetooth). We may also receive location information from you when you choose to share such information on our Services, including by associating your content with a location, or we may derive your approximate location from other information about you, including your IP address. If you authorize or link a third-party service (e.g., an unofficial mobile app client) to access your Reddit account, Reddit receives information about your use of that service when it uses that authorization. Linking services may also cause the other service to send us information about your account with that service. For example, if you sign in to Reddit with a third-party identity provider, that provider may share an email address with us. To learn how information is shared with linked services, see “How Information About You Is Shared” below. We also may receive information about you, including log and usage data and cookie information, from third-party sites that integrate our Services, including our embeds and advertising technology. For example, when you visit a site that uses Reddit embeds, we may receive information about the web page you visited. Similarly, if an advertiser incorporates Reddit’s ad technology, Reddit may receive limited information about your activity on the advertiser’s site or app, such as whether you bought something from the advertiser. You can control how we use this information to personalize the Services for you as described in “Your Choices - Controlling Advertising and Analytics” below Reddit displays some linked content in-line on the Reddit services via “embeds.” For example, Reddit posts that link to YouTube or Twitter may load the linked video or tweet within Reddit directly from those services to your device so you don’t have to leave Reddit to see it. In general, Reddit does not control how third-party services collect data when they serve you their content directly via these embeds. As a result, embedded content is not covered by this privacy policy but by the policies of the service from which the content is embedded. We partner with third-party programmatic ad exchanges to show advertisements relevant to your interests. In providing those ads, those third parties collect information, including log and usage data and information from cookies as described above. These third parties do not receive any information from your Reddit account. We partner with audience measurement companies (including Quantcast and Nielsen) to learn demographic information about the population that uses Reddit. To provide this demographic information, these companies collect cookie information to recognize your device. If you use Reddit Ads (Reddit’s self-serve ads platform at ads.reddit.com) we collect some additional information. To sign up for Reddit Ads, you must provide your name, email address, and information about your company. If you purchase advertising services, you will need to provide transactional information as described above, and we may also require additional documentation to verify your identity. When using Reddit Ads, we may record a session replay of your visit for customer service, troubleshooting, and usability research purposes. If you choose to link or sign up using your social network (such as Facebook, Twitter, Instagram, or Google), we may collect information from these social media services, including your contact lists for these services and information relating to your use of the Platform in relation to these services. We may collect information about you from third-party services, such as advertising partners and analytics providers. We may collect information about you from other publicly available sources. We collect information about the device you use to access the Platform, including your IP address, unique device identifiers, model of your device, your mobile carrier, time zone setting, screen resolution, operating system, app and file names and types, keystroke patterns or rhythms, and platform.We collect information about your location, including location information based on your SIM card and/or IP address. With your permission, we may also collect Global Positioning System (GPS) data. We collect and process, which includes scanning and analyzing, information you provide in the context of composing, sending, or receiving message through the Platform’s messaging functionality. That information includes the content of the message and information about when the message has been sent, received and/or read, as well as the participants of the communication. Please be aware that messages sent to other users of the Platform will be accessible by those users and that we are not responsible for the manner in which those users use or disclose messages. We and our service providers and business partners use cookies and other similar technologies (e.g. web beacons, flash cookies, etc.) (“Cookies”) to automatically collect information, measure and analyze which web pages you click on and how your use the Platform, enhance your experience using the Platform, improve the Platform, and provide you with targeted advertising on the Platform and elsewhere across your different devices. Cookies are small files which, when placed on your device, enable the Platform to provide certain features and functionality. Web beacons are very small images or small pieces of data embedded in images, also known as “pixel tags” or “clear GIFs,” that can recognize Cookies, the time and date a page is viewed, a description of the page where the pixel tag is placed, and similar information from your computer or device. To learn how to disable Cookies, see your “Your choices” section below. Additionally, we allow these service providers and business partners to collect information about your online activities through Cookies. We and our service providers and business partners link your contact or subscriber information with your activity on our Platform across all your devices, using your email or other log-in or device information. Our service providers and business partners may use this information to display advertisements on our Platform and elsewhere  online and across your devices tailored to your interests, preferences, and characteristics. We are not responsible for the privacy practices of these service providers and business partners, and the information practices of these service providers and business partners are not covered by this Privacy Policy. We may aggregate or de-identify the information described above. Aggregated or de-identified data is not subject to this Privacy Policy. We share the categories of personal information listed above with service providers and business partners to help us perform business operations and for business purposes, including research, payment processing and transaction fulfillment, database maintenance, administering contests and special offers, technology services, deliveries, email deployment, advertising, analytics, measurement, data storage and hosting, disaster recovery, search engine optimization, marketing, and data processing. These service providers and business partners may include: Payment processors and transaction fulfillment providers, who may receive the information you choose to provide, the information we obtain from other sources, and the information we collect automatically but who do not receive your message data. Customer and technical support providers, who may receive the information you choose to provide, the information we obtain from other sources, and the information we collect automatically. Researchers, who may receive the information you choose to provide, the information we obtain from other sources, and the information we collect automatically but would not receive your payment information or message data. Cloud providers, who may receive the information you choose to provide, the information we obtain from other sources, and the information we collect automatically. Advertising, marketing, and analytics vendors, who may receive the information you choose to provide, the information we obtain from other sources, and the information we collect automatically but would not receive your payment information or message data. We retain your information for as long as it is necessary to provide you with the service so that we can fulfil our contractual obligations and exercise our rights in relation to the information involved. Where we do not need your information in order to provide the service to you, we retain it only as long as we have a legitimate business purpose in keeping such data or where we are subject to a legal obligation to retain the data. We will also retain your data if necessary for legal claims. For more information, click here."


def train_spacy(data, iterations):
    TRAIN_DATA = data
    nlp = spacy.blank('en')  # create blank Language class
    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)

    # add labels
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(iterations):
            print("Statring iteration " + str(itn))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update(
                    [text],  # batch of texts
                    [annotations],  # batch of annotations
                    drop=0.2,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            print(losses)
    return nlp


prdnlp = train_spacy(TRAIN_DATA, 20)

# Save our trained Model
modelfile = input("Enter your Model Name: ")
prdnlp.to_disk(modelfile)

# Test your text
#test_text = input("Enter your testing text: ")
test_text = TEST_DATA
doc = prdnlp(test_text)
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)