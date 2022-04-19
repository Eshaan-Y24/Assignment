# Django-React Full-Stack app
The project was an assignment for an e-commerce startup that required a simple UI to input a string and display products based on the input text. 
![input with debouncing implemented](images/input_debouncing.gif)<br/>
The search bar has a debouncing function for the input text, built using setTimeout. This prevents rapid api calling, and relieves the backend off load.<br/><br/><br/>

![tab changes](images/tabs.gif)<br/>
The results can be queried with category tabs as well. Selecting a category queries all the products within the same category.<br/><br/><br/>

![models schema](images/models.png)<br />
The django model looks like this. A foriegn key is used to link categories and products<br/><br/><br/>

![products json](images/products.png)<br />
The models are hosted as json objects

![categories json](images/categories.png)<br />
The models are hosted as json objects
