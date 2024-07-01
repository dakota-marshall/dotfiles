local telescope = require('telescope')

vim.keymap.set({"n","x"}, "p", "<Plug>(YankyPutAfter)")
vim.keymap.set({"n","x"}, "P", "<Plug>(YankyPutBefore)")
vim.keymap.set({"n","x"}, "gp", "<Plug>(YankyGPutAfter)")
vim.keymap.set({"n","x"}, "gP", "<Plug>(YankyGPutBefore)")

vim.keymap.set("n", "<c-p>", "<Plug>(YankyPreviousEntry)")
vim.keymap.set("n", "<c-n>", "<Plug>(YankyNextEntry)")

-- Load the yank_history plugin for Telescope
require("telescope").load_extension("yank_history")
vim.keymap.set("n", "<leader>k", telescope.extensions.yank_history.yank_history, {})

-- Highlight yank and puts
require("yanky").setup({
  highlight = {
    on_put = true,
    on_yank = true,
    timer = 500,
  },
})
