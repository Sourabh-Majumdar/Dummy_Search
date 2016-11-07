% This is the page_rank module
% Here I will load up the Matrix and calculate the Page Rank
% and then this will be uploaded on the database
% --------------------------------------------------------------

X = load("dataset.txt")
Y = X(:,2:end)
m = size(X,1)
page_rank = 1/m*ones(1,m)
for i = 1:10,
 page_rank = page_rank * Y
end
my_file = page_rank'
save "page_rank.txt" my_file