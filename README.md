# VaxFlow

How equitable is access across the country? Attempt to create a visualization of the COVID19 vaccine supply chain access pieced together using multiple sources of data.

## Rationale

We initially wanted to display supply chain data, but decided to tightly focus on just distribution, which we felt was the most important. Our first idea was, user enters a zip-code: "02141" and a date, and it tells you how many people did you skip over to cut the line. A sad way to virtue signal. Instead, we flipped it to show how distribution is going by race.

We chose to use a map encoding since the vaccine data was is geographically distributed. It also provides an intuitive sense of how things are moving temporaly, which areas need attention and how multiple locations form clusters of vaccination surges (perhaps due to local events.). We also chose to use a timeline slider to manipulate the data, being able to scrub, and softly animate the changes allows for a very stark contrast on the difference between vaccine access.

Data wrangling was really hard, we had to piece together multiple sources of data, hidden in powerpoint slides to obscure excel sheets. Implementing the matrix transforms for map movement was also non-trivial. Josh did the hard wrangling and Shreyas did the hard linear algebra.

TO-DO:
- Add scales! Especially for colors.
- Add tooltips for each zip-code, detailed breakdown.
- Use our full data on race.
- Add a zip-code search to make it personal.


## Development

First time setup,

```
cd vis
npm install
```

Then, for local development,

```
npm run serve
```

## Deployment

Auto gh-pages deployment coming soon.
