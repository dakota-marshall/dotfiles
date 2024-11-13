vim.g.mapleader = " "
vim.keymap.set("n", "<leader>pv", vim.cmd.NvimTreeOpen)

-- Move Selection in visual mode
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

-- Keep cursor center in search
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

vim.keymap.set("x", "<leader>p", [["_dP]])

-- Replace all instances of word under curosr
vim.keymap.set("n", "<leader>s", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]])

-- Make current file executable
vim.keymap.set("n", "<leader>x", "<cmd>!chmod +x %<CR>", { silent = true })

-- Execute current file
vim.keymap.set("n", "<leader>X", "<cmd>!%:p<CR>")

-- Debugger Mappings
vim.keymap.set("n", "<leader>db", "<cmd> DapToggleBreakpoint <CR>")
vim.keymap.set(
    "n",
    "<leader>dpr",
    function()
        require("dap-python").test_method()
    end
)

-- Error browsing
vim.keymap.set("n", "<leader>e", vim.diagnostic.goto_next, opts)
vim.keymap.set("n", "<leader>a", vim.lsp.buf.code_action, opts)
