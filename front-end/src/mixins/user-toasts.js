const toasts = {
  methods: {
    errorToast(msg) {
        this.$toast.open({
          duration: 5000,
          message: msg,
          position: 'is-bottom',
          type: 'is-danger',
        });
    },
    successToast(msg) {
        this.$toast.open({
          duration: 5000,
          message: msg,
          position: 'is-bottom',
          type: 'is-success',
        });
    },
  },
};

export { toasts };