
    // Set the event date (for example, the 2026 FIFA World Cup start date)
    const eventDate = new Date("June 11, 2026 00:00:00").getTime();

    // Update countdown every second
    const countdown = setInterval(function() {
        const now = new Date().getTime();
        const timeLeft = eventDate - now;

        // Calculate time remaining
        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        // Update the countdown in the DOM
        document.querySelector(".days").innerText = days + " days";
        document.querySelector(".hours").innerText = hours + " hours";
        document.querySelector(".minutes").innerText = minutes + " mins";
        document.querySelector(".seconds").innerText = seconds + " secs";

        // If the countdown is finished
        if (timeLeft < 0) {
            clearInterval(countdown);
            document.querySelector(".countdown").innerText = "The event has started!";
        }
    }, 1000); // Update every 1000ms (1 second)