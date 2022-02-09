module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        maincolor: "#87CEEB",
        headercolor: "#F6FDFF",
      },
      boxShadow: {
        readmoreShadow: "0 0 10 0 rgba(0,0,0,0.3)",
      },
      gridTemplateColumns: {
        colsAutoFill: "repeat(auto-fill, minmax(16em, 1fr))",
      },
    },
  },
  variants: {
    extend: {
      brightness: ["hover", "group-hover"],
      visibility: ["hover", "group-hover"],
    },
  },
  plugins: [],
};
