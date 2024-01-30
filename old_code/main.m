
%% Script to attempt to naive process Aiptasia images.

A = importdata("IMG_2619.jpg"); % Load in image.

B = mean(A(:,:,:),3); % Convert to greyscale.
B = B./255; % Normalise.

I = 1-B;

[~,threshold] = edge(I,'sobel');
fudgeFactor = 0.3;
BWs = edge(I,'sobel',threshold * fudgeFactor);

se90 = strel('line',3,90);
se0 = strel('line',3,0);

BWsdil = imdilate(BWs,[se90 se0]);
imshow(BWsdil)

imshow(BWsdil)

% threshHigh = 1;
% threshLow = 0;
% B( B(:,:) >= threshHigh) = 1;
% B( B(:,:) <= threshLow) = 0;
%imagesc(gradient(B))

%%


%% Script to attempt to naive process Aiptasia images.

A = importdata("IMG_5809.jpg"); % Load in image.

B = mean(A(:,:,:),3); % Convert to greyscale.
B = B./255; % Normalise.

I = 1-B;

% threshHigh = 1;
 threshLow = 0.7;
% B( B(:,:) >= threshHigh) = 1;
 I( I(:,:) <= threshLow) = 0;

 [~,threshold] = edge(I,'sobel');
fudgeFactor = 0.1;
BWs = edge(I,'sobel',threshold * fudgeFactor);

se90 = strel('line',3,90);
se0 = strel('line',3,0);


BWsdil = imdilate(BWs,[se90 se0]);
imshow(BWsdil)

% [centers,radii] = imfindcircles(I,[5 15],"ObjectPolarity","bright");
 % 
 % BWoutline = bwperim(I);
 % Segout = I;
 % Segout(BWoutline) = 255;
 % imshow(Segout)

%imagesc(I);
