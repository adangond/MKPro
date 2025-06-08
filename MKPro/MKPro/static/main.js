document.addEventListener("DOMContentLoaded", function() {
    const toggles = document.querySelectorAll(".submenu-toggle");
    
    toggles.forEach(toggle => {
        toggle.addEventListener("click", function(event) {
            event.preventDefault();
            event.stopPropagation();

            const submenu = this.nextElementSibling;

            // 🔹 Verifica si el submenú actual ya está abierto
            const isOpen = submenu.classList.contains("hidden");

            // 🔹 Cierra todos los submenús antes de abrir uno nuevo
            document.querySelectorAll(".submenu").forEach(menu => {
                menu.classList.add("hidden");
            });

            // 🔹 Alternar visibilidad del submenú actual solo si estaba cerrado
            if (isOpen) {
                submenu.classList.remove("hidden");
            }
        });
    });

    // 🔹 Cerrar submenús si el usuario hace clic fuera
    document.addEventListener("click", function(event) {
        if (!event.target.closest(".submenu-toggle") && !event.target.closest(".submenu")) {
            document.querySelectorAll(".submenu").forEach(menu => {
                menu.classList.add("hidden");
            });
        }
    });

    console.log("MKPro está listo y con menú optimizado! 🚀");
});