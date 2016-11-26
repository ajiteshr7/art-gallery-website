CREATE TABLE IF NOT EXISTS Ref_payment_methods (
  payment_method_code  	int(11)	  NOT NULL,
  payment_method_description  	VARCHAR(30)   	NOT NULL,
  PRIMARY KEY (payment_method_code)
);
Insert into Ref_payment_methods values (001,'Credit Card'),(002,'Debit Card'),(003,'Paypal'),(004,'VISA'),(005,'Bank Draft');

CREATE TABLE IF NOT EXISTS Customers (
  buyer_id			int(11)	NOT NULL,
  organization_name		VARCHAR(30)	NOT NULL,
  gender			VARCHAR(30)	NOT NULL,
  first_name			VARCHAR(30)	NOT NULL,
  middle_initial		VARCHAR(30)	NOT NULL,
  last_name			VARCHAR(30)	NOT NULL,
  email_address			VARCHAR(30)	NOT NULL,
  login_name			VARCHAR(30)	NOT NULL,
  login_password		VARCHAR(30)	NOT NULL,
  phone_number			VARCHAR(30)	NOT NULL,
  address_line_1		VARCHAR(50)	NOT NULL,
  address_line_2		VARCHAR(50)	NOT NULL,
  address_line_3		VARCHAR(50)	NOT NULL,
  address_line_4		VARCHAR(50)	NOT NULL,
  town_city			VARCHAR(30)	NOT NULL,
  country			VARCHAR(30)	NOT NULL,
  PRIMARY KEY (buyer_id)
);

Insert into Customers values
(4251,'Calliart','M','Greg','C','Carter','greg0666@gmail.com','gcarter','gc0707','40289423','731 Fondren','Houston','TX','-','Texas','United States'),
(4253,'GarrisonArt','M','John','L','Albert','johann@gmail.com','johnalbert','albert123','40244423','83 Berry','Bellaire','TX','-','Texas','United States');


CREATE TABLE IF NOT EXISTS Ref_painting_status (
  status_code  		     int(11)	NOT NULL,
  status_description  	VARCHAR(30)   	NOT NULL,
  PRIMARY KEY (status_code)
);

Insert into Ref_painting_status values (1,'Complete'),(2,'Under Progress'),(3,'Proposition');

CREATE TABLE IF NOT EXISTS Ref_movements (
  movement_code  		int(11)	NOT NULL,
  movement_description  	VARCHAR(30)   	NOT NULL,
  PRIMARY KEY (movement_code)
);


Insert into Ref_movements values (1,'Delivered'),(2,'Out to Deliver'),(3,'Undelivered');

CREATE TABLE IF NOT EXISTS Ref_order_item_status_codes (
  order_item_status_code  		int(11)	NOT NULL,
  order_item_status_description  	VARCHAR(30)   	NOT NULL,
  PRIMARY KEY (order_item_status_code)
);

Insert into Ref_order_item_status_codes values (1,'Packed'),(2,'Shipping'),(3,'Shipped');

CREATE TABLE IF NOT EXISTS Ref_order_status_codes (
  order_status_code  		int(11)	NOT NULL,
  order_status_description  	VARCHAR(30)   	NOT NULL,
  PRIMARY KEY (order_status_code)
);

Insert into Ref_order_status_codes values (1,'Confirmed'),(2,'Pending');

CREATE TABLE IF NOT EXISTS Ref_invoice_status_codes (
  invoice_status_code  		int(11)	NOT NULL,
  invoice_status_description  	VARCHAR(30)   	NOT NULL,
  PRIMARY KEY (invoice_status_code)
);

Insert into Ref_invoice_status_codes values (1,'Generated'),(2,'Under Progress'),(3,'Delivered');

CREATE TABLE IF NOT EXISTS Ref_categories (
  category_code  		int(11)	NOT NULL,
  parent_category_code  	int(11)	NOT NULL,
  category_description  	VARCHAR(30)   	NOT NULL,
  PRIMARY KEY (category_code),
  FOREIGN KEY (parent_category_code) REFERENCES Ref_painting_status(status_code)
);

Insert into Ref_categories values (1,1,'Drawing'),(2,1,'Sketch'),(3,1,'Sculpture');

CREATE TABLE IF NOT EXISTS Customer_payment_methods (
  customer_payment_id		int(11)	NOT NULL,
  customer_id			int(11)	NOT NULL,
  payment_method_code  	int(11)	NOT NULL,
  credit_card_number            VARCHAR(30)	NOT NULL,
  payment_method_details  	VARCHAR(30)   	NOT NULL,
  PRIMARY KEY (payment_method_code),
  FOREIGN KEY (customer_id) REFERENCES Customers(buyer_id),
  FOREIGN KEY (payment_method_code) REFERENCES Ref_payment_methods(payment_method_code)
);

Insert into Ref_categories values (525,4251,002,'1234123412341234','Debit Card'),
(526,4253,003,'1356846756789033','Paypal'),
(527,4251,001,'1123355545645673','Credit Card');

CREATE TABLE IF NOT EXISTS Artists (
  artist_id			int(11)	NOT NULL,
  movement_code     int(11)	NOT NULL,
  artist_name   		VARCHAR(30)	NOT NULL,
  artist_photo   		LONGBLOB	NOT NULL,
  artist_bio    		VARCHAR(100)	NOT NULL,
  place_of_birth		VARCHAR(30)	NOT NULL,
  country 			VARCHAR(30)	NOT NULL,
  date_of_birth 		VARCHAR(30)	NOT NULL,
  date_deceased 		VARCHAR(30)	NOT NULL,
  typical_price_range($)		VARCHAR(30)	NOT NULL,
  other_details    		VARCHAR(100)	NOT NULL,
  PRIMARY KEY (artist_id),
  FOREIGN KEY (movement_code) REFERENCES Ref_movements(movement_code)
);

Insert into Artists values (555,2,'S. Bernardie',profile.png,'Artst at SpringField Ind.','TownHall','US','24-07-1973','-','500-800','-');

CREATE TABLE IF NOT EXISTS Paintings (
  painting_id			int(11)	NOT NULL,
  painting_photo   LONGBLOB NOT NULL,
  artist_id			int(11)	NOT NULL,
  category_code     int(11)	NOT NULL,
  painting_status_code		int(11)	NOT NULL,
  title 			VARCHAR(30)	NOT NULL,
  buying_price			VARCHAR(30)	NOT NULL,
  selling_price			VARCHAR(30)	NOT NULL,
  size(square inches)		VARCHAR(30)	NOT NULL,
  description    		VARCHAR(100)	NOT NULL,
  PRIMARY KEY (painting_id),
  FOREIGN KEY (artist_id) REFERENCES Artists(artist_id),
  FOREIGN KEY (category_code) REFERENCES Ref_categories(category_code),
  FOREIGN KEY (painting_status_code) REFERENCES Ref_painting_status(status_code)
);

Insert into Paintings values (429,painting1.jpg,555,1,2,'Blossoms','300','500','8.5*4','Awareness,Motivational,Artwork');

CREATE TABLE IF NOT EXISTS Shopping_cart (
  painting_id  		int(11)	NOT NULL,
  buyer_id  		int(11)	NOT NULL,
  date_added		VARCHAR(30)	NOT_NULL,
  PRIMARY KEY (buyer_id,painting_id),
  FOREIGN KEY (buyer_id) REFERENCES Customers(buyer_id),
  FOREIGN KEY (painting_id) REFERENCES Paintings(painting_id)
);

Insert into Shopping_cart values (4251,429,'03-07-2015');

CREATE TABLE IF NOT EXISTS Orders (
  order_id  		int(11)	NOT NULL,
  buyer_id  		int(11)	NOT NULL,
  order_status_code	int(11)	NOT_NULL,
  date_order_placed	VARCHAR(30)	NOT_NULL,
  order_details		VARCHAR(30)	NOT_NULL,
  PRIMARY KEY (order_id),
  FOREIGN KEY (buyer_id) REFERENCES Customers(buyer_id),
  FOREIGN KEY (order_status_code) REFERENCES Ref_order_status_codes(order_status_code)
);

Insert into Orders values (4251,429,2,'05-02-2016','Shipped');

CREATE TABLE IF NOT EXISTS Invoices (
  invoice_number	int(11)	NOT NULL,
  order_id  		int(11) 	NOT NULL,
  invoice_status_code	int(11)	NOT NULL,
  invoice_date		VARCHAR(30)	NOT NULL,
  invoice_details	VARCHAR(30)	NOT NULL,
  PRIMARY KEY (invoice_number),
  FOREIGN KEY (order_id) REFERENCES Orders(order_id),
  FOREIGN KEY (invoice_status_code) REFERENCES Ref_invoice_status_codes(invoice_status_code)
);

Insert into Invoices values (4251,429,2,'07-06-2016','Generated');

CREATE TABLE IF NOT EXISTS Shipments (
  shipment_id			int(11)	NOT NULL,
  order_id  			int(11)	NOT NULL,
  invoice_number		int(11)	NOT NULL,
  shipment_tracking_number	int(11)	NOT NULL,
  shipment_date			VARCHAR(30)	NOT NULL,
  other_shipment_details	VARCHAR(30)	NOT NULL,
  PRIMARY KEY (shipment_id),
  FOREIGN KEY (order_id) REFERENCES Orders(order_id),
  FOREIGN KEY (invoice_number) REFERENCES Invoices(invoice_number)
);

Insert into Shipments values (4251,429,2,4342972,'07-06-2016','Packaged,Out for Delivery'),(4251,429,2,4342972,'07-06-2016','Packaged,Out for Delivery'),(4251,429,2,4342972,'07-06-2016','Packaged,Out for Delivery');

CREATE TABLE IF NOT EXISTS Order_items (
  order_item_id			int(11)	NOT NULL,
  product_id  			int(11)  	NOT NULL,
  order_id  			int(11)	NOT NULL,
  order_item_status_code	int(11)	NOT NULL,
  order_item_quantity		int(11)	NOT NULL,
  order_item_price		VARCHAR(30)	NOT NULL,
  other_order_item_details	VARCHAR(30)	NOT NULL,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (product_id) REFERENCES Paintings(painting_id),
  FOREIGN KEY (order_id) REFERENCES Orders(order_id),
  FOREIGN KEY (order_item_status_code) REFERENCES Ref_order_item_status_codes(order_item_status_code)
);

Insert into Order_items values (4251,429,2,4342972,7,'Rs. 350','-'),(4251,429,2,4342972,7,'Rs. 350','-'),(4251,429,2,4342972,7,'Rs. 350','-');

CREATE TABLE IF NOT EXISTS Payments (
  payment_id  		int(11)	NOT NULL,
  invoice_number  	int(11)   	NOT NULL,
  payment_date		VARCHAR(30)   	NOT NULL,
  payment_amount	VARCHAR(30)   	NOT NULL,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (invoice_number) REFERENCES Invoices(invoice_number)
);

Insert into Payments values (2434,429,'23-05-2016','Rs. 550'),(2434,429,'23-05-2016','Rs. 550'),(2434,429,'23-05-2016','Rs. 550');

CREATE TABLE IF NOT EXISTS Shipment_items (
  shipment_id  		int(11)	NOT NULL,
  order_item_id 	int(11)	NOT NULL,
  PRIMARY KEY (shipment_id,order_item_id),
  FOREIGN KEY (shipment_id) REFERENCES Shipments(shipment_id),
  FOREIGN KEY (order_item_id) REFERENCES Order_items(order_item_id)
);

Insert into Shipment_items values (2434,42),(2442,21),(2439,33),(2436,65),(2435,78),(2433,97);
