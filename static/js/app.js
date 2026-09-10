/* =========================================================
   AGRI-NEXUS - JAVASCRIPT
========================================================= */

document.addEventListener("DOMContentLoaded", function () {

    /* =====================================================
       1. AUTO HIDE ALERT MESSAGES
    ===================================================== */

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {

        setTimeout(function () {

            alert.style.opacity = "0";
            alert.style.transform = "translateY(-10px)";
            alert.style.transition = "0.4s";

            setTimeout(function () {
                alert.remove();
            }, 400);

        }, 4500);

    });


    /* =====================================================
       2. FILE UPLOAD NAME
    ===================================================== */

    const fileInputs = document.querySelectorAll(
        'input[type="file"]'
    );

    fileInputs.forEach(function (input) {

        input.addEventListener("change", function () {

            if (this.files.length > 0) {

                const fileName = this.files[0].name;

                const preview =
                    document.querySelector("[data-file-name]");

                if (preview) {
                    preview.textContent =
                        "Selected file: " + fileName;
                }

            }

        });

    });


    /* =====================================================
       3. CONFIRM BUTTON
    ===================================================== */

    const confirmButtons =
        document.querySelectorAll("[data-confirm]");

    confirmButtons.forEach(function (button) {

        button.addEventListener("click", function (event) {

            const message =
                this.getAttribute("data-confirm");

            if (!confirm(message)) {
                event.preventDefault();
            }

        });

    });


    /* =====================================================
       4. ANIMATED COUNTERS
    ===================================================== */

    const counters =
        document.querySelectorAll("[data-counter]");

    counters.forEach(function (counter) {

        const target =
            parseInt(counter.getAttribute("data-counter"));

        if (isNaN(target)) return;

        let current = 0;

        const increment =
            Math.max(1, Math.ceil(target / 60));

        const timer = setInterval(function () {

            current += increment;

            if (current >= target) {
                current = target;
                clearInterval(timer);
            }

            counter.textContent =
                current.toLocaleString();

        }, 20);

    });


    /* =====================================================
       5. SMOOTH SCROLL
    ===================================================== */

    const scrollLinks =
        document.querySelectorAll('a[href^="#"]');

    scrollLinks.forEach(function (link) {

        link.addEventListener("click", function (event) {

            const targetId =
                this.getAttribute("href");

            if (targetId === "#") return;

            const target =
                document.querySelector(targetId);

            if (target) {

                event.preventDefault();

                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });

            }

        });

    });


    /* =====================================================
       6. SCROLL TO TOP
    ===================================================== */

    const scrollTop =
        document.getElementById("scrollTop");

    if (scrollTop) {

        window.addEventListener("scroll", function () {

            if (window.scrollY > 400) {

                scrollTop.style.display = "flex";
                scrollTop.style.alignItems = "center";
                scrollTop.style.justifyContent = "center";

            } else {

                scrollTop.style.display = "none";

            }

        });


        scrollTop.addEventListener("click", function () {

            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });

        });

    }


    /* =====================================================
       7. DRAG & DROP IMAGE UPLOAD
    ===================================================== */

    const uploadZone =
        document.querySelector(".upload-zone");

    const uploadInput =
        document.querySelector(
            '.upload-zone input[type="file"]'
        );

    if (uploadZone && uploadInput) {

        uploadZone.addEventListener(
            "dragover",
            function (event) {

                event.preventDefault();

                uploadZone.style.borderColor =
                    "#18c77a";

            }
        );


        uploadZone.addEventListener(
            "dragleave",
            function () {

                uploadZone.style.borderColor =
                    "rgba(255,255,255,0.3)";

            }
        );


        uploadZone.addEventListener(
            "drop",
            function (event) {

                event.preventDefault();

                uploadZone.style.borderColor =
                    "#18c77a";

                if (event.dataTransfer.files.length > 0) {

                    uploadInput.files =
                        event.dataTransfer.files;

                    uploadInput.dispatchEvent(
                        new Event("change")
                    );

                }

            }
        );

    }


    /* =====================================================
       8. PASSWORD SHOW / HIDE
    ===================================================== */

    const passwordToggle =
        document.querySelector(
            "[data-password-toggle]"
        );

    if (passwordToggle) {

        passwordToggle.addEventListener(
            "click",
            function () {

                const input =
                    document.querySelector(
                        "[data-password]"
                    );

                if (!input) return;

                if (input.type === "password") {

                    input.type = "text";
                    this.textContent = "Hide";

                } else {

                    input.type = "password";
                    this.textContent = "Show";

                }

            }
        );

    }


    /* =====================================================
       9. CURRENT YEAR
    ===================================================== */

    const year =
        document.querySelector("[data-year]");

    if (year) {
        year.textContent =
            new Date().getFullYear();
    }


    /* =====================================================
       10. CARD REVEAL ANIMATION
    ===================================================== */

    const cards =
        document.querySelectorAll(".card");

    cards.forEach(function (card, index) {

        card.style.opacity = "0";
        card.style.transform = "translateY(15px)";
        card.style.transition =
            "opacity 0.5s ease, transform 0.5s ease";

        setTimeout(function () {

            card.style.opacity = "1";
            card.style.transform = "translateY(0)";

        }, 100 + (index * 70));

    });


    /* =====================================================
       11. SEARCH FILTER FOR TABLES
    ===================================================== */

    const searchInput =
        document.querySelector("[data-table-search]");

    if (searchInput) {

        searchInput.addEventListener("input", function () {

            const value =
                this.value.toLowerCase();

            const rows =
                document.querySelectorAll(
                    "table tbody tr"
                );

            rows.forEach(function (row) {

                const text =
                    row.textContent.toLowerCase();

                if (text.includes(value)) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }

            });

        });

    }


    /* =====================================================
       12. IMAGE PREVIEW
    ===================================================== */

    const imageInput =
        document.querySelector(
            "[data-image-input]"
        );

    const imagePreview =
        document.querySelector(
            "[data-image-preview]"
        );

    if (imageInput && imagePreview) {

        imageInput.addEventListener("change", function () {

            const file = this.files[0];

            if (!file) return;

            if (!file.type.startsWith("image/")) {
                return;
            }

            const reader =
                new FileReader();

            reader.onload = function (event) {

                imagePreview.src =
                    event.target.result;

                imagePreview.style.display =
                    "block";

            };

            reader.readAsDataURL(file);

        });

    }


    /* =====================================================
       13. LOADING STATE FOR FORMS
    ===================================================== */

    const forms =
        document.querySelectorAll("form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function () {

            const submitButton =
                this.querySelector(
                    'button[type="submit"]'
                );

            if (submitButton) {

                submitButton.disabled = true;

                const originalText =
                    submitButton.textContent;

                submitButton.textContent =
                    "Processing...";

                setTimeout(function () {

                    submitButton.disabled = false;

                    submitButton.textContent =
                        originalText;

                }, 5000);

            }

        });

    });

});