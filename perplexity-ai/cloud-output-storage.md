# Cloud output storage for Perplexity AI

29-Dec-24

## **1. Tool/Software Name**

Perplexity AI Pro. 

---

## **2. Feature Title**

Cloud storage integration for better output management. 

---

## **3. Description of the Feature**
 
 Perplexity AI has made some good investment in its library functionality, allowing users to save specific outputs into folders. It's adopting a parallel process to that being seen in ChatGPT, in a sense, which at the time of writing recently rolled out a projects feature intended to allow users to aggregate specific outputs into folders. 

---

## **4. Problem or Need Addressed**
 
While being able to save your outputs into a library populated within the platform is useful, it's not a sufficient or ideal solution for many users.  

- Unless the platform specifically provides an API for users to access their own data, this aggregated data cannot be integrated into 3rd party systems. Let's say that a user is using Perplexity in order to do some research that might be useful if it were recorded in a knowledge management tool. The store of outputs in Perplexity just becomes another data silo for the team. Those who do not have accounts are locked out of accessing it. 
- From a backup perspective, managing data in this way is also very weak. Without programmatic access, users are not able to duplicate this data onto onsite or managed storage. And there's no meaningful ability to back up what could be an important trove of data for the business. 
- The concept of the output library being wedded to the LLM frontend or access platform  reflects a design philosophy in which the output of AI systems and work continued by humans should be Rigidly separated. But a more accurate reflection of emerging workflows is that the outputs of AI systems and their continuation by humans is one deeply interlinked data store.  Gathering all of this information into one platform, like a cloud workspace makes more sense. 
---

## **5. Benefits of the Feature**

### Increased exposure to AI tools
 
 A robust system for connecting Perplexity AI to other cloud data stores would firstly greatly increase the utility of the tool in business contexts. More internal resources could be exposed to the value of data derived from AI, which might in turn actually drive more seats. 

### More convenient than doing this through workarounds

 It would allow the outputs of AI systems to be embedded into organized business workflows without having to consider cumbersome tools for bringing external AI tools into existing tools such as Google Docs. Rather, outputs could be piped seamlessly into a target folder in, let's say, a Google Drive. This would enable a workflow in which the AI outputs arrive into a standard folder and can then be taken forward for internal business use. 

 ### AI outputs can be backed up

 This would also greatly bolster the confidence of technical system administrators in feeling a sense of ownership over data that currently is siloed in the Perplexity library. Once the data gets duplicated to a system that is already covered by a backup process, such as a cloud workspace tool, the data can be properly protected by existing backup policies. 

### Would reflect emerging AI-human workflows

 Increasingly, AI outputs are seen as first drafts for continued iteration by humans. For this reason, copying them into a target like a Google Drive also makes sense and reflects the way in which these systems are actually used while alleviating the tedious work of users in copying data out of Perplexity, creating documents in a matching cloud system, and then pasting into them.  If this task could be automated through a preconfigured workflow, the time savings would accrue over time and make for a much more seamless embedding of AI tools into business workflows.

---

## **6. Suggested Implementation (Optional)**
 
Here are a few creative suggestions for how this could be implemented:

### Save to cloud button

A button added next to the copy icon at the bottom of AI outputs which will automatically copy the chat, including the prompt and the output into the default target folder in cloud storage.

### Context button for other clouds

If the feature were to cover adding multiple clouds as connected data sources, then a context menu could be added in which the user is able to manually select the target cloud every time they perform the operation.  This would allow the user to be able to write different outputs to different clouds. 

### Automatic copying versus manual copying

If an interface were added in which the user could manage their connected cloud storages, they could also perhaps choose between automatically copying the library to a connected cloud or manually doing it through the UI feature as suggested above. This would allow the same core feature to cater for different preferences in workflow. 

### Automatic formatting

If threads could be saved to attached external cloud storages through the integration described above some. Simple back end logic could be configured to format the documents most appropriately. 

As Perplexity already automatically provides a summary of the conversation, this could be chosen as the document title when the thread is being written to the external storage. There could perhaps be a summary section added containing a very short executive summary of the thread. 

Bold font could be used to distinguish between prompts and AI responses. 

The document could contain a header section containing the key parameters of the thread recording data such as the time it was generated, the specific model used to generate the thread, and perhaps the username of the user to assist with identification.  

Bold font could Or other formatting elements could be used to visually distinguish between user prompts and AI responses, especially useful in threads which contain a number of follow up questions.

In a down the road implementation, perhaps users could even create their own template based upon common elements in threads. Or in a less ambitious implementation Perplexity could provide a default template which users could modify using drag and drop elements. For instance, they may wish to put the header section as a footer appearing on every page of the generated document. 

Target formats could even be specified so users could choose whether to write the created documents as Markdown. PDF or perhaps for every save-to-cloud operation it could be generated in all formats. 

### Prompt library generation

Given that perplexity already distinguishes between user prompts and AI responses with targeted copying elements, it would be possible, presumably to automatically generate a prompt library in a target external cloud storage. This could be achieved by extracting only the prompts from threads and giving them a descriptive title in automatically generated folder within the cloud target. 

Similar to the suggestions for overall thread management, there could be context elements used to provide user with some control over how this data is copied. Perhaps all prompts could automatically be copied to the prompt library. Or in a parallel to the above suggestion for threads only specific prompts could be deliberately copied by clicking on a UI element. 

---

**7. Additional Notes or References**

Adding robust features for routing Perplexity threads into external cloud storages could greatly enhance the utility of the tool by embedding it into business processes. 
