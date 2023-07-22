create table users(
	UserId serial primary key,
	UserName varchar(255) not null unique, 
	Password varchar(255) not null
);

create table product(
	ProductId serial primary key,
	ProductName varchar(255) not null,
	Price integer not null,
	Quantity integer not null
);

create table orders(
	OrderId serial primary key,
	UserId integer,
	foreign key (UserId) references users(UserId)
);

create table order_item(
	ItemId bigserial primary key,
	ProductId integer,
	OrderId integer,
	foreign key (ProductId) references product(ProductId),
	foreign key (OrderId) references orders(OrderId)
);