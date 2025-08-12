local lsp_zero = require('lsp-zero')

lsp_zero.on_attach(function(client, bufnr)
    -- see :help lsp-zero-keybindings
    -- to learn the available actions
    lsp_zero.default_keymaps({ buffer = bufnr })
    lsp_zero.buffer_autoformat()
end)

require('mason').setup({
    ensure_installed = {
        "black",
        "ruff",
        "debugpy",
        "mypy"
    }
})
require('mason-lspconfig').setup({
    ensure_installed = {
        "ansiblels",
        "gopls",
        "pyright",
    },
    handlers = {
        lsp_zero.default_setup,
    },
})
-- require('lspconfig').pico8_ls.setup({
--     capabilities = capabilities,
--     cmd = {
--         'pico8-ls',
--         '--stdio'
--     },
--     filetypes = { "p8", 'pico8', 'lua' },
-- })
