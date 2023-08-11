create table users(
	userid  serial primary key,
	username varchar(255) not null unique,
	password varchar(255) not null
);

create table product(
	productid serial primary key,
	productName varchar(255) not null,
	price integer not null,
	quantity integer not null
);

create table orders(
	orderid serial primary key,
	userid integer,
	price integer not null,
	foreign key (userId) references users(userId)
);

create table order_item(
	itemid serial primary key,
	productid integer,
	orderid integer,
	quantity integer not null,
	price integer not null,
	productname varchar(255) not null,
	foreign key (productId) references product(productid),
	foreign key (orderId) references orders(orderid)
);